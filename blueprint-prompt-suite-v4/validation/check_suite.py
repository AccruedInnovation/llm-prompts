#!/usr/bin/env python3
"""Read-only checks of this prompt release, not an evaluator of model behavior.

Run with Python 3.9+: python validation/check_suite.py
Optional: --baseline-root PATH checks preservation and diffs against the exact
input filenames used for this release. Those old inputs are not in the archive.
"""
from __future__ import annotations

import argparse
import difflib
import re
import sys
from pathlib import Path
from typing import List, Tuple

PROMPTS = [
    "01-systems-design-planner-prompt-v4.md",
    "02-systems-design-planner-adversarial-review-prompt-v4.md",
    "03-blueprint-architecture-design-package-synthesizer-prompt-v4.md",
    "04-blueprint-architecture-design-package-adversarial-review-prompt-v4.md",
    "05-PRD-implementability-authoring-prompt-v4.md",
    "06-PRD-implementability-adversarial-review-prompt-v4.md",
    "implementation/blueprint-bbk-one-shot-implementation-prompt-v4.md",
    "implementation/blueprint-bbk-one-shot-implementation-prompt-v4-compact.md",
]
BASELINES = [
    "systems-design-prompts-territories-r1/systems-design-planner-prompt-v3.md",
    "systems-design-prompts-territories-r1/systems-design-planner-adversarial-review-prompt-v2.md",
    "architecture-design-prompts-territories-r1/blueprint-architecture-design-package-synthesizer-prompt-v3.md",
    "architecture-design-prompts-territories-r1/blueprint-architecture-design-package-adversarial-review-prompt-v2.md",
    "prd-prompts-territories-r1/PRD-implementability-authoring-prompt-v3.md",
    "prd-prompts-territories-r1/PRD-implementability-adversarial-review-prompt-v2.md",
    "blueprint-bbk-one-shot-implementation-prompt-v3(1).md",
    "blueprint-bbk-one-shot-implementation-prompt-v3-compact(1).md",
]
PLANNER_FIELDS = [
    "design_brief_id", "revision", "scope_id", "purpose_and_scope",
    "input_maturity", "target_maturity", "operating_limits", "selected_direction",
    "controlling_refs", "fixed_decision_refs", "decision_record", "evidence_refs",
    "architecture_assignment", "open_items", "artifact_inventory", "approval_state", "readiness",
]
PRD_FIELDS = [
    "id", "architecture_baseline", "capability_ids", "outcome", "scope",
    "allocated_requirement_ids", "contribution_obligations", "fixed_refs",
    "delegated_design", "required_elaboration", "dependencies", "acceptance_obligations",
    "integration_owner", "final_acceptance_owner", "authoring_environment",
    "review_policy", "open_items", "readiness",
]
PRD_HEADINGS = [
    "Status and decision summary", "Repository discovery and current state",
    "Outcome, scope, and non-goals", "Interfaces and data contracts",
    "Canonical production and verification closure", "Bootstrap, staging, and migration",
    "State, effects, transactions, and recovery", "Source, install, runtime, and platform closure",
    "Integration, invalidation, and requalification", "Test and evidence plan",
    "Leaf implementation slices", "Risks, security, operations, and documentation", "Implementability matrix",
]
MATRIX = [
    "Repository or new-project evidence, baseline, and current-state discovery",
    "Architecture binding, allocated scope, delegated design, and approval gates",
    "Target maturity, operating limits, and permitted claims",
    "Source precedence, design authority, and decision closure",
    "Outcome, scope, non-goals, and ownership",
    "Target worker, context fit, and bounded local choices",
    "Interfaces and field-level data contracts",
    "Canonical producer/recomputation/verifier closure",
    "Cross-artifact admission and consistency where required",
    "Non-circular bootstrap, staging, and migration",
    "State/effect/transaction/recovery semantics",
    "Source/build/install/runtime/platform closure",
    "Observed capabilities and filesystem boundaries",
    "Integration invalidation and requalification",
    "Author-set acceptance rules and schema-valid adversarial cases",
    "Supplied artifacts, reference availability, and author-time validation",
    "Leaf slices, file ownership, sequencing, and dispatch gates",
    "Worker-facing handoffs and fresh-context recipient review",
    "Set-equal allocated/local obligation coverage and cross-PRD acceptance ownership",
    "Open facts, decisions, assumptions, and late-bound values",
    "Security, operations, rollout, and documentation",
]


def outside_code(text: str) -> Tuple[str, bool]:
    lines, fence = [], None
    for line in text.splitlines():
        found = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
        if found:
            mark, tail = found.groups()
            if fence is None:
                fence = (mark[0], len(mark))
            elif mark[0] == fence[0] and len(mark) >= fence[1] and not tail.strip():
                fence = None
            continue
        if fence is None:
            lines.append(line)
    return "\n".join(lines), fence is None


def section(text: str, heading: str) -> str:
    start = text.index(heading)
    level = len(heading) - len(heading.lstrip("#"))
    match = re.search(r"(?m)^#{1," + str(level) + r"} ", text[start + len(heading):])
    end = start + len(heading) + match.start() if match else len(text)
    return text[start:end].strip()


def paragraph(text: str, prefix: str) -> str:
    start = text.index(prefix)
    end = text.find("\n\n", start)
    return text[start:end if end >= 0 else len(text)].strip()


def common_until(text: str, prefix: str, last_sentence: str) -> str:
    start = text.index(prefix)
    end = text.index(last_sentence, start) + len(last_sentence)
    return text[start:end]


def matrix_rows(text: str) -> List[str]:
    lines = outside_code(text)[0].splitlines()
    start = next(i for i, line in enumerate(lines) if line.startswith("| Dimension |"))
    rows = []
    for line in lines[start + 2:]:
        if not line.startswith("|"):
            break
        rows.append(line.split("|")[1].strip())
    return rows


def check_suite(root: Path, baseline_root: Path | None) -> int:
    checks: List[Tuple[str, bool, str]] = []

    def check(name: str, ok: bool, detail: str = "") -> None:
        checks.append((name, bool(ok), detail))

    texts = []
    for rel in PROMPTS:
        path = root / rel
        check("exists: " + rel, path.is_file())
        if not path.is_file():
            print("FAIL missing prompt:", rel, file=sys.stderr)
            return 1
        texts.append(path.read_text(encoding="utf-8"))
    check("root workflow order 01..06", [p.name for p in sorted(root.glob("[0-9][0-9]-*.md"))] == PROMPTS[:6])
    check("exactly eight released prompt files", sorted(str(p.relative_to(root)) for p in root.rglob("*prompt*.md")) == sorted(PROMPTS))

    for rel, text in zip(PROMPTS, texts):
        clean, closed = outside_code(text)
        check("v4 metadata: " + rel, text.count("**Version:** 4 ·") == 1 and text.count("**Set revision:** `harmonized-v4`") == 1)
        check("balanced code fences: " + rel, closed)
        check("no stale active suite metadata: " + rel, "coordinated-r1" not in text and "**Stage amendment:**" not in text and not re.search(r"\*\*(?:Version|Revision):\*\* [123]", text))
        check("UTF-8 text, newline, no NUL: " + rel, text.endswith("\n") and "\x00" not in text and "\ufffd" not in text)
        # Markdown tables: remove code spans/escaped pipes before counting separators.
        width, issues = None, []
        for n, line in enumerate(clean.splitlines(), 1):
            if line.startswith("|"):
                masked = re.sub(r"`+[^`]*`+", "CODE", line).replace(r"\|", "PIPE")
                count = len(masked.split("|")) - 2
                if width is None:
                    width = count
                elif count != width:
                    issues.append(n)
            else:
                width = None
        check("Markdown table widths: " + rel, not issues, str(issues))
        enum_values = {"EXPLICIT_APPROVAL", "DELEGATED_AUTHORITY", "PROVISIONAL_WORKING", "APPROVAL_REQUIRED"}
        check("authority vocabulary: " + rel, all("`" + val + "`" in text for val in enum_values))

    for i, count in [(1, 17), (2, 28), (3, 23), (5, 26), (6, 18), (7, 18)]:
        numbers = [int(n) for n in re.findall(r"(?m)^## (\d+)\. ", outside_code(texts[i])[0])]
        check("numbered sections: " + PROMPTS[i], numbers == list(range(1, count + 1)), str(numbers))

    for i in [0, 1]:
        # Check canonical field declarations specifically in the handoff table.
        block = section(texts[i], "### Consolidated working design brief" if i == 0 else "## 12. Review the architecture-authoring handoff")
        fields = []
        for line in block.splitlines():
            if line.startswith("| `"):
                fields.extend(re.findall(r"`([^`]+)`", line.split("|")[1]))
        check("17 exact planner handoff fields: " + PROMPTS[i], fields == PLANNER_FIELDS, str(fields))
    for i in [2, 3, 4, 5]:
        check("18 architecture-to-PRD fields: " + PROMPTS[i], all(re.search(r"\b" + re.escape(f) + r"\b", texts[i]) for f in PRD_FIELDS))
    for i in [4, 5]:
        check("21 exact PRD matrix rows: " + PROMPTS[i], matrix_rows(texts[i]) == MATRIX)
    headings = re.findall(r"(?m)^### \d+\. (.+)$", outside_code(section(texts[4], "## Required PRD output"))[0])
    check("13 exact main PRD headings", headings == PRD_HEADINGS, str(headings))
    repeated = section(texts[5], "### B. Complete revised PRD and supporting packet")
    check("reviewer preserves ordered PRD headings", re.findall(r"(?m)^\d+\. (.+)$", repeated) == PRD_HEADINGS)
    self_questions = re.findall(r"(?m)^(\d+)\. ", section(texts[4], "## Mandatory self-review before responding"))
    check("12 PRD self-review questions", self_questions == [str(n) for n in range(1, 13)])

    shared = [section(texts[i], "## Shared workflow rules") for i in [0, 2, 4]]
    check("identical shared workflow rules in authors", len(set(shared)) == 1)
    contexts = [paragraph(t, "**Context accounting.**") for t in texts]
    check("identical full-context accounting across eight prompts", len(set(contexts)) == 1)
    integrity = [common_until(t, "Use existing revisions or stable snapshots and a concise change record during content work.", "This document policy does not weaken required product integrity checks or pre-execution verification of supplied tools.") for t in texts]
    check("identical document-integrity policy across eight prompts", len(set(integrity)) == 1)
    completions = [common_until(texts[i], "Separate review assessment, required-check completion,", "Where missing sources prevent a status assessment, retain the candidate's status only as an unverified claim.") for i in [1, 3, 5]]
    check("identical missing-prerequisite/review-completion rule", len(set(completions)) == 1)
    fresh = [common_until(texts[i], "Before claiming PRD implementation readiness,", "not the routine missing-review rule.") for i in [4, 5]]
    check("identical mandatory per-slice fresh-recipient rule", len(set(fresh)) == 1)
    check("identical bounded trial rule", section(texts[4], "### Bounded target-worker trial") == section(texts[5], "### Bounded target-worker trial"))
    check("trial is not self-prerequisite", "not its own entry prerequisite" in texts[4] and "all other applicable design, recipient-review, safety, and execution gates remain binding" in texts[4])

    for label in ["### Territory handoff and review continuity", "## 16. Final candidate and artifact integrity", "### Continuation and interruption", "### Reference availability and dispatch", "### Protect acceptance semantics", "### Exact-subject rule and observations", "### Delivery and acceptance status", "## 18. Required final response and result record", "## 1. Mission and implementation posture", "## 2. Authority and source precedence", "## 11. Discovered work and specification defects", "## 13. Planned-versus-actual conformance", "## 15. Progress communication"]:
        check("executor full/compact shared contract: " + label, section(texts[6], label) == section(texts[7], label))
    for i in [6, 7]:
        check("executor preserves required evidence and product integrity: " + PROMPTS[i], all(s in texts[i] for s in ["final digest", "pre-execution verification of supplied tools", "Executor self-review cannot replace mandatory fresh-recipient evidence", "required package digests"]))
    check("compact remains shorter than full", len(texts[7].split()) < len(texts[6].split()))

    # Links in release documents (not illustrative Markdown strings inside code blocks).
    link_issues, link_count = [], 0
    for path in root.rglob("*.md"):
        clean = outside_code(path.read_text(encoding="utf-8"))[0]
        for target in re.findall(r"\[[^\]\n]+\]\(([^)]+)\)", clean):
            if re.match(r"(?:https?:|mailto:|#)", target):
                continue
            link_count += 1
            dest = target.split("#", 1)[0]
            resolved = (path.parent / dest).resolve()
            if root.resolve() not in [resolved, *resolved.parents] or not resolved.exists():
                link_issues.append(str(path.relative_to(root)) + ": " + target)
    check("relative links resolve inside delivery root", not link_issues, "; ".join(link_issues))
    print("INFO relative links checked:", link_count)

    # Constructed rehearsal arithmetic, not a model or prompt-behavior test.
    demands, capacity = [40, 40, 40], 100
    check("fixture: every pair fits but aggregate does not", all(demands[i] + demands[j] <= capacity for i in range(3) for j in range(i + 1, 3)) and sum(demands) > capacity)
    check("fixture: corrected allocation fits", sum([30, 30, 30]) <= capacity)
    parent = {"ingest", "display", "recovery", "integrated-acceptance"}
    children = {"ingest", "display"}
    retained = {"recovery", "integrated-acceptance"}
    check("fixture: split detects omitted duties", parent - children == retained)
    check("fixture: explicit retained duties close allocation", children | retained == parent)
    graph = {"contract": {"A", "B", "C", "integrated"}, "A-local": {"A"}, "A": {"recipient-A"}, "B": {"recipient-B"}, "C": {"recipient-C"}}
    def affected(node: str) -> set:
        result, pending = set(), [node]
        while pending:
            current = pending.pop()
            for child in graph.get(current, set()):
                if child not in result:
                    result.add(child)
                    pending.append(child)
        return result
    check("fixture: local invalidation remains local", affected("A-local") == {"A", "recipient-A"})
    check("fixture: shared change reaches counterparts and integration", affected("contract") == {"A", "B", "C", "integrated", "recipient-A", "recipient-B", "recipient-C"})

    if baseline_root:
        for i, (rel, oldrel) in enumerate(zip(PROMPTS, BASELINES)):
            oldpath = baseline_root / oldrel
            check("baseline available: " + rel, oldpath.is_file())
            if not oldpath.is_file():
                continue
            old = oldpath.read_text(encoding="utf-8")
            before = re.findall(r"(?m)^## \d+\. .+$", outside_code(old)[0])
            after = re.findall(r"(?m)^## \d+\. .+$", outside_code(texts[i])[0])
            check("numbered source sections preserved: " + rel, before == after)
            old_enums = set(re.findall(r"`([A-Z][A-Z0-9_]+)`", old))
            new_enums = set(re.findall(r"`([A-Z][A-Z0-9_]+)`", texts[i]))
            check("source uppercase contract values retained: " + rel, old_enums <= new_enums, str(old_enums - new_enums))
            diff = "".join(line if line.endswith("\n") else line + "\n\\ No newline at end of file\n" for line in difflib.unified_diff(old.splitlines(True), texts[i].splitlines(True), fromfile="before/" + oldrel, tofile="after/" + rel, n=3))
            diffpath = root / "notes" / "diffs" / (Path(rel).stem + ".diff")
            check("exact supplied-source diff: " + rel, diffpath.is_file() and diffpath.read_text(encoding="utf-8") == diff)
        old_planner = (baseline_root / BASELINES[0]).read_text(encoding="utf-8")
        check("Systems Design Compass unchanged", texts[0][texts[0].index("# Systems Design Compass"):].strip() == old_planner[old_planner.index("# Systems Design Compass"):].strip())
        old_prd = (baseline_root / BASELINES[4]).read_text(encoding="utf-8")
        before_questions = re.findall(r"(?m)^\d+\. .+$", section(old_prd, "## Mandatory self-review before responding"))
        after_questions = re.findall(r"(?m)^\d+\. .+$", section(texts[4], "## Mandatory self-review before responding"))
        check("all twelve PRD self-review questions unchanged", before_questions == after_questions)
    else:
        print("NOT RUN source-comparison checks: no --baseline-root supplied")

    # Parse the illustrative YAML only when PyYAML exists; no importer/schema claim.
    try:
        import yaml
    except ImportError:
        print("NOT RUN illustrative YAML parse: optional PyYAML unavailable")
    else:
        blocks = re.findall(r"(?ms)^```yaml\n(.*?)^```", texts[2])
        try:
            class UniqueKeyLoader(yaml.SafeLoader):
                pass
            def unique_mapping(loader, node, deep=False):
                mapping = {}
                for key_node, value_node in node.value:
                    key = loader.construct_object(key_node, deep=deep)
                    if key in mapping:
                        raise ValueError("duplicate YAML key: " + str(key))
                    mapping[key] = loader.construct_object(value_node, deep=deep)
                return mapping
            UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)
            data = [yaml.load(block, Loader=UniqueKeyLoader) for block in blocks]
            check("illustrative YAML syntax and duplicate keys", len(data) == 1 and isinstance(data[0], dict))
            check("illustrative YAML preserves exactly 18 assignment keys", list(data[0]["prd_assignments"][0]) == PRD_FIELDS)
        except (yaml.YAMLError, ValueError, KeyError, IndexError, TypeError) as exc:
            check("illustrative YAML syntax and shape", False, str(exc))

    for name, ok, detail in checks:
        print(("PASS " if ok else "FAIL ") + name + ((": " + detail) if detail and not ok else ""))
    failures = sum(not ok for _, ok, _ in checks)
    print(f"SUMMARY {len(checks) - failures}/{len(checks)} checks passed; {failures} failed")
    print("LIMIT These checks cover release structure, selected policy agreement, and constructed fixture calculations. They do not establish semantic completeness, model performance, independent review, or end-to-end workflow success.")
    return 1 if failures else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--baseline-root", type=Path)
    args = parser.parse_args()
    try:
        return check_suite(args.root.resolve(), args.baseline_root.resolve() if args.baseline_root else None)
    except (OSError, ValueError, StopIteration) as exc:
        print("FAIL unable to complete checks: " + str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

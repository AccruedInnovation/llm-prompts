# Harmonization and validation notes

**Suite:** `harmonized-v4` · **Date:** 2026-09-08  
**Disposition:** Eight complete replacement prompts, candidate for workflow trials. This report does not grant approval to any product design or implementation.

## Basis and scope

The pass used the six current territory revisions, both supplied implementation-executor editions, the accepted harmonization plan, and the supplied Process and Coordination Philosophy. It did not use external research or amend the philosophy. Earlier planning/design/PRD sources remain untouched. All eight released prompts use version 4 and one set revision; the six design/review filenames sort 01–06. The two alternative executors sit in a separate folder, not additional numbered design stages.

The root README names the use order. Each prompt remains self-contained for its duties; paired source contracts and task-specific governing material must still be available when a conformance finding depends on them. Release notes, diffs, examples, and checker are optional support, not another mandatory workflow layer.

## Changes and dispositions

| Area | v4 change | Preserved boundary |
| --- | --- | --- |
| Shared rules | Condensed and matched the three authoring blocks. | Stage responsibilities, decision origin/authority, evidence, questions, effects, and local invalidation remain distinct. |
| Context accounting | Matched the complete-context rule across all eight prompts; reduced repeated territory/scheduling explanations. | Required governing detail, parent duties, review coverage, and output/working reserve cannot disappear to make a task fit. |
| Missing prerequisite | Matched the three reviewers' distinction between assessment of a demonstrated gap and completion of the missing check. | Unreviewed work and interrupted rechecks remain unfinished; a diagnosis does not confer readiness, assurance, or acceptance. |
| Integrity | Matched optional final document-checksum policy; removed mandatory architecture-archive hashing and routine unversioned draft-hash fallback. | Required product integrity, pre-execution supplied-tool verification, final implementation-artifact binding, and affected rechecks remain. |
| Recipient review | Matched the complete PRD author/reviewer rule, questions, per-slice exposure, evidence reuse, and repair handling. | Every slice still needs valid fresh-recipient evidence before PRD `PASS`; same-context self-review is not a substitute. |
| Worker trial | Matched trial permission, bounded experimental design, observations, and non-circular entry requirements. | A separate complete experiment does not make its incomplete parent executable, approved, or accepted. |
| Executor intake | Added territory lineage, reading routes, parent duties, shared-change consequences, and evidence continuity to both editions. | The executor follows supplied design and slices, preserves acceptance, and routes shared changes to their owner. |
| Release navigation | Renamed active references and all prompt headers to v4; preserved earlier-edition handling. | Renaming a suite does not supersede actual product decisions or invalidate still-valid prior evidence. |

The common review rule permits a finished assessment of known unavailable inputs only with evidence, scoped effects, an owner, and a closure method. It does not license labeling unread material examined. Required checks and repairs remain visibly unsatisfied until the missing work actually runs.

The trial clarification treats the suitability claim as the output of a separately authorized complete experiment. It does not remove other applicable recipient-review, design, safety, authority, or execution gates, and avoids a trial whose entry prerequisite is its own result.

## Cross-stage checks

| Boundary | Review performed | Result and limits |
| --- | --- | --- |
| Planner → architecture | Compared selected direction, fixed/delegated questions, territory inheritance, reading routes, shared-definition order, and 17 planner handoff fields with architecture intake. | No requirement to settle every local schema at planning; direction-changing unknowns still prevent dependent commitments. Author-only semantic comparison. |
| Architecture → PRD | Compared all 18 assignment fields, dependency phases, canonical contract ownership, allocation, and semantic acceptance responsibilities. | Needed shared definitions must exist before dependent design; fully specified future code can wait until dispatch. Author-only semantic comparison plus field checks. |
| PRD → executor | Compared design/approval/dispatch separation, four worker-reference classes, acceptance ownership, packet fit, inherited duties, and review-evidence reuse. | `PARTIAL`/`BLOCKED` parent PRDs cannot dispatch convenient child slices; separately authorized complete scopes retain their own gates. Author-only semantic comparison. |
| Author → reviewer → successor | Compared revision authority, unchanged-subject review, canonical repairs, affected rechecks, gap dispositions, and earlier-edition handling. | No automatic transfer of the author's personal authority or prior approval. Unverified repairs cannot claim closure. Author-only semantic comparison. |
| Local → boundary → integrated claim | Checked counterpart assumptions, aggregate constraints, joined traces, and compatible evidence revisions. | Local or pairwise passes do not establish a spanning outcome. Constructed counterexamples and bounded calculations, not product execution. |
| Full → compact executor | Compared matched authority, dispatch, continuation, acceptance protection, observations, specification-defect route, divergence rules, final integrity, result/status, and new intake sections. | These selected sections match exactly. Remaining explanations received an author-only comparison; no claim of identical model behavior. |

## Preserved source structure

The planner retains its decision reports, blocking-decision test, 17 handoff fields, and unchanged Systems Design Compass text (the output adds a final newline). The architecture author retains its 28 numbered sections and 18 PRD-assignment fields. Its review retains 23 numbered sections; the systems reviewer retains 17.

The PRD author retains all 13 main PRD headings, the exact 21 matrix rows, and all twelve source self-review questions unchanged. Its review retains 26 numbered sections and the same 21 matrix labels. Both executors retain their 18 numbered sections and seven final-response sections. Source uppercase contract values remain present; this lexical check does not by itself prove semantic equivalence.

Intentional differences remain: planning readiness uses `READY_FOR_ARCHITECTURE`; architecture assignments use `READY_FOR_PRD`; PRDs use `PASS`/`PARTIAL`/`BLOCKED`; dispatch uses `READY`/`NOT_READY`/`NOT_ASSESSED`. Approval, observed check outcomes, effect permission, and implementation acceptance remain separate. The first two stages do not acquire the PRD stage's mandatory fresh-recipient gate.

## Instruction size

Whitespace-separated word counts, not token counts or measured model capacity:

| Prompt | Before | v4 | Change |
| --- | ---: | ---: | ---: |
| 1 | 6,315 | 5,860 | -455 |
| 2 | 9,201 | 9,316 | +115 |
| 3 | 12,652 | 12,340 | -312 |
| 4 | 11,965 | 11,914 | -51 |
| 5 | 9,761 | 9,535 | -226 |
| 6 | 14,451 | 14,135 | -316 |
| Executor full | 7,853 | 8,377 | +524 |
| Executor compact | 5,404 | 6,006 | +602 |

The six design/review prompts fell from **64,345 to 63,100 words**, a reduction of **1,245 words (1.93%)**. The complete eight-prompt set fell from **77,602 to 77,483 words**. Executor intake and integrity clarification account for most of the added text. This is targeted consolidation, not a substantial compression of the whole set; context benefits remain to be measured. No new compact design/review editions were added.

## Validation performed

The read-only checker covers prompt inventory and order, v4 metadata, code-fence balance, table widths, source section numbering, authority values, handoff fields, PRD headings/matrix, shared policy agreement, selected full/compact executor contracts, relative links, source diffs, and the unchanged Compass/self-review questions. With installed PyYAML it parsed the one illustrative architecture handoff, used a duplicate-key-rejecting loader, and checked its 18 assignment keys. That is syntax and shape checking, not schema or importer qualification.

The initial checker wrongly demanded inline-code formatting around every architecture-to-PRD field in the PRD author's input list. The names and meanings already existed in a permitted format. The checker was corrected to accept exact field names without demanding backticks; the prompts were not changed to invent that formatting requirement. Link checks then remained open until all referenced release-support files existed. Final results and delivery checks appear below. A separate replay check also exposed a missing end-of-file marker in the planner diff because its input lacked a final newline. The diff writer now emits the standard marker; replay succeeds without changing the prompt content to satisfy the checker.

The [rehearsal](../examples/rehearsal-cases.md) records fifteen author-only analytical cases using one tiny task and one three-territory fixture with controlled variations. The checker executes six bounded checks of capacity arithmetic, obligation sets, and graph reachability. They test fixture calculations, not an agent's interpretation of a prompt.

No separate reviewer agent, fresh-recipient run, intended-worker implementation trial, six-stage model run, or large-package benchmark ran. Static agreement and this author's walkthrough do not establish complete semantic equivalence, defect-detection performance, reduced context failures, product correctness, or production readiness.

## Source mapping and diffs

Paths below identify the supplied baselines used for this release; they are not required runtime locations. Old prompt files are not copied into the consolidated archive. Each diff compares the exact named input with its v4 replacement.

| Released file | Supplied baseline | Evidence |
| --- | --- | --- |
| `01-systems-design-planner-prompt-v4.md` | `systems-design-prompts-territories-r1/systems-design-planner-prompt-v3.md` | [Diff](diffs/01-systems-design-planner-prompt-v4.diff) |
| `02-systems-design-planner-adversarial-review-prompt-v4.md` | `systems-design-prompts-territories-r1/systems-design-planner-adversarial-review-prompt-v2.md` | [Diff](diffs/02-systems-design-planner-adversarial-review-prompt-v4.diff) |
| `03-blueprint-architecture-design-package-synthesizer-prompt-v4.md` | `architecture-design-prompts-territories-r1/blueprint-architecture-design-package-synthesizer-prompt-v3.md` | [Diff](diffs/03-blueprint-architecture-design-package-synthesizer-prompt-v4.diff) |
| `04-blueprint-architecture-design-package-adversarial-review-prompt-v4.md` | `architecture-design-prompts-territories-r1/blueprint-architecture-design-package-adversarial-review-prompt-v2.md` | [Diff](diffs/04-blueprint-architecture-design-package-adversarial-review-prompt-v4.diff) |
| `05-PRD-implementability-authoring-prompt-v4.md` | `prd-prompts-territories-r1/PRD-implementability-authoring-prompt-v3.md` | [Diff](diffs/05-PRD-implementability-authoring-prompt-v4.diff) |
| `06-PRD-implementability-adversarial-review-prompt-v4.md` | `prd-prompts-territories-r1/PRD-implementability-adversarial-review-prompt-v2.md` | [Diff](diffs/06-PRD-implementability-adversarial-review-prompt-v4.diff) |
| `blueprint-bbk-one-shot-implementation-prompt-v4.md` | `blueprint-bbk-one-shot-implementation-prompt-v3(1).md` | [Diff](diffs/blueprint-bbk-one-shot-implementation-prompt-v4.diff) |
| `blueprint-bbk-one-shot-implementation-prompt-v4-compact.md` | `blueprint-bbk-one-shot-implementation-prompt-v3-compact(1).md` | [Diff](diffs/blueprint-bbk-one-shot-implementation-prompt-v4-compact.diff) |

## Stop condition

The bounded harmonization pass stops after supported conflicts are reconciled, preserved source contracts and active references check out, the constructed valid/defective cases have explicit outcomes, and the actual consolidated archive matches its delivery tree. Remaining work is behavioral testing, not another automatic rewrite or metadata-repair cycle.

## Final check record

This section records final observed checks; it is not a product or PRD readiness verdict.

| Check | Observed result | Scope |
| --- | --- | --- |
| Release checks with exact earlier inputs | 141 of 141 passed. | Structure, selected policy agreement, source-contract preservation, links, fixture calculations, and illustrative YAML. |
| Standalone checks from the delivery tree | 107 of 107 passed. | Same self-contained checks, excluding earlier-input comparisons. |
| Diff replay | All 8 applied with `patch --fuzz=0`; each result matched its v4 file byte for byte. | Delivered diffs against the named supplied inputs. |
| Consolidated archive | 21 files; CRC check passed, paths stayed within one root, and every extracted file matched the delivery tree byte for byte. | Actual final archive, not an assumed file list. |
| Fresh-extraction check | 107 of 107 standalone checks passed from a separate extraction. | Relative references and release checks remained usable after transfer. |

Environment: Python 3.13.5, PyYAML 6.0.3, and the installed `patch` utility. The checker installs nothing and invokes no model. No content-hash manifest or detached checksum was produced. Archive integrity here means extraction and byte comparison, not a claim of external provenance.

Commands used, with the task's actual locations substituted for these explanatory paths:

```text
python validation/check_suite.py --baseline-root <supplied-input-root>
python validation/check_suite.py
patch --batch --silent --fuzz=0 -o <temporary-output> <exact-input> <delivered-diff>
```

The archive checks also used Python's standard-library ZIP reader, safe-path inspection, a temporary extraction, and direct byte comparisons. The fresh extraction ran the included checker without a baseline argument. No generated product, external service, or model workflow was exercised.

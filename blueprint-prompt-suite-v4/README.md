# Blueprint prompt suite v4

**Set revision:** `harmonized-v4` · **Date:** 2026-09-08  
**Status:** Candidate for workflow trials. Structural checks and an author-only harmonization review have run; independent-agent and large-package workflow trials have not.

## Use order

The six root prompts sort in the normal author → review → next-stage order. Each is a complete replacement, not an amendment to append to an earlier prompt.

| Order | Prompt | Use |
| --- | --- | --- |
| 01 | [Systems Design Planner](01-systems-design-planner-prompt-v4.md) | Select the direction and assign bounded architecture work. |
| 02 | [Systems Design Adversarial Review](02-systems-design-planner-adversarial-review-prompt-v4.md) | Review and repair the planning output within authority. |
| 03 | [Architecture and Design Package Synthesizer](03-blueprint-architecture-design-package-synthesizer-prompt-v4.md) | Settle shared architecture and assign bounded PRD scopes. |
| 04 | [Architecture Adversarial Review](04-blueprint-architecture-design-package-adversarial-review-prompt-v4.md) | Review and repair shared design, boundaries, allocation, and handoffs. |
| 05 | [PRD Author](05-PRD-implementability-authoring-prompt-v4.md) | Complete detailed design, acceptance materials, and implementation slices. |
| 06 | [PRD Adversarial Review](06-PRD-implementability-adversarial-review-prompt-v4.md) | Review and repair the complete PRD packet and check every slice's recipient evidence. |

The review prompts review **outputs**, not the paired authoring prompt. The authoring prompt supplies their conformance contract. Make that contract available for exact-clause retrieval; do not automatically load both full prompts and the complete project history into every helper's context.

Start at the stage justified by the available material. Small tasks may combine stages when they meet each applicable obligation. The numbering does not require six separate agents, sessions, approvals, or document layers. A review report does not itself approve a package. Continue only the scopes whose actual readiness and phase-specific permissions support the next assignment.

## Implementation after the design stages

Both executor editions are included at v4 in `implementation/`, outside the requested 01–06 design/review sequence:

| Edition | File |
| --- | --- |
| Full | [One-Shot Implementation Executor v4](implementation/blueprint-bbk-one-shot-implementation-prompt-v4.md) |
| Compact | [One-Shot Implementation Executor v4 — Compact](implementation/blueprint-bbk-one-shot-implementation-prompt-v4-compact.md) |

Choose **one** executor edition, not both. Each works on its own and shares the same authority, entry gates, protected acceptance rules, and result requirements. The compact edition shortens explanation; it is not a less strict execution mode.

Give the executor the authorized PRD, assigned slices, accessible canonical inputs, required review evidence, actual dependencies, and effect permissions. Preserve the supplied decomposition and reading routes. Do not dispatch selected children of an overall `PARTIAL` or `BLOCKED` PRD. An independently authorized complete sub-scope or trial has its own obligations and gates.

## What v4 reconciles

The prompts now agree on full-context accounting, inherited territory duties, document-integrity policy, and the distinction between a completed assessment of a missing prerequisite and a completed check. The PRD pair shares the same per-slice fresh-recipient and bounded-trial instructions. Both executors preserve the revised handoffs and valid review evidence without repeating upstream design by default.

Intentional stage differences remain. Planning hands bounded architecture choices forward; architecture settles shared behavior and delegates local detail; PRDs must complete worker-level design. Fresh-recipient review remains conditional at the first two stages and mandatory for every PRD slice before `PASS`. Design readiness, package approval, dispatch readiness, observations, execution permission, and implementation acceptance remain separate.

Earlier adequate inputs remain usable under their actual governing edition. Do not retrofit formatting defects or invalidate evidence solely because the prompt suite changed. New v4 obligations apply when the assignment adopts them; substantive old requirements still apply on their original basis.

## Optional guidance and checks

[Harmonization and validation notes](notes/HARMONIZATION-AND-VALIDATION.md) document the edits, source editions, preserved rules, size changes, and evidence limits. [Bounded-review assignment example](examples/bounded-review-assignment.md) shows how to delegate an exact question without forwarding the entire lead context. [Rehearsal cases](examples/rehearsal-cases.md) provide valid and defective cases for the first agent trials, plus the author-only analytical results.

These files and the diffs are release support material, not required additions to each agent's instructions or each generated package. No old prompts, territory amendment, external shared-policy file, or Blueprint installation is needed to use the replacements. Supply any project-specific governing sources the task requires.

Run the read-only release checks from this directory with Python 3.9 or later:

```text
python validation/check_suite.py
```

The checker uses the standard library; it also parses the illustrative architecture YAML when PyYAML is already available. It does not install dependencies or invoke a model. It checks selected release contracts, not arbitrary generated PRDs or architectural correctness. Optional `--baseline-root` checks need the exact earlier input filenames listed in the script; those inputs remain outside this archive.

No detached archive checksum or recurring document-hash manifest is included. The archive's contents and extraction were checked. Product integrity and supplied-tool verification rules remain in the executor prompts.

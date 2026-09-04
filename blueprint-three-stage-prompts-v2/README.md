# Blueprint three-stage prompt set — v2

**Set revision:** coordinated-r1  
**Date:** 2026-09-04  
**Status:** review draft

This set applies the changes agreed in the conversation to the supplied planner, architecture synthesizer, and implementation-ready PRD author. Each prompt is complete and standalone. This README is a usage and review guide, not a fourth authoring stage or a required source of hidden instructions.

## Prompts

| Stage | Prompt | Responsibility and output |
| --- | --- | --- |
| 1 | [Systems Design Planner](prompts/systems-design-planner-prompt-v2.md) | Develop and select a responsible direction; deliver a current working design brief, decision record, evidence, and bounded architecture assignment. |
| 2 | [Architecture and Design Package Synthesizer](prompts/blueprint-architecture-design-package-synthesizer-prompt-v2.md) | Complete and check the shared architecture; deliver a versioned baseline, canonical contracts, requirement allocation, and PRD-authoring assignments. |
| 3 | [Implementation-Ready PRD Author](prompts/PRD-implementability-authoring-prompt-v2.md) | Complete detailed design for an assigned scope; supply implementation contracts, fixtures, expected results, checks, and worker-sized slices. |

The split follows the decisions each recipient needs settled. It does not forbid detailed early design. Later authors must reuse sound earlier decisions, exact contracts, fixtures, and evidence rather than recreate them.

## How to use the set

For a new idea, use the planner with the idea, known constraints, available guidance, and decision/effect permissions. At completion, carry its consolidated brief and actual supporting artifacts—not merely its final response—to the architecture author.

Use the synthesizer with that brief or directly with an existing discussion corpus. Name the current design or source baseline, task mode, target maturity, authority, output location, and permitted effects. The result identifies each PRD scope, controlling obligations, delegated detail, dependencies, and acceptance ownership.

Use the PRD prompt once per coherent assignment, or for one small complete system. Supply the assignment and the relevant accessible architecture/contracts, repository or confirmed new-project state, worker capability profile, and authoring/review permissions. Later PRDs must inspect the real accepted predecessor outputs they depend on. Do not assume the original architecture-era code snapshot is still current.

A bounded change under an adequate architecture can start at the PRD stage. An extensive discussion with a clear direction can start at the synthesizer. A small task may combine responsibilities in one session or document while retaining the distinct checks. A justified no-build recommendation may end after planning.

## Two different kinds of maturity

**Input maturity** describes how much is known: an idea, partial design, discussion corpus, or accepted baseline. **Target maturity** describes what will be delivered: an experiment, bounded prototype, or production-intended system.

A prototype narrows obligations through explicit scope and operating limits; it does not leave implemented behavior undefined. A learning experiment can receive its own complete architecture and PRD scope before the final production design is settled. Its results return to the relevant design decision and do not count as broad production qualification.

## Handoff contracts

The planner's final **working design brief** has named fields for current scope, direction, decision authority, evidence, open items, actual artifacts, and the architecture assignment.

The architecture's **PRD-authoring assignment** identifies its baseline, allocated requirements and contributions, fixed references, delegated design, required elaboration, dependencies, acceptance obligations, integration and final acceptance owners, review policy, and readiness. Machine-readable YAML is optional unless the assignment requires it. It is a projection, not a claimed match for an existing importer.

The PRD returns a bound result with allocated coverage, detailed decisions, actual artifacts and checks, shared-change findings, and separate design, approval, and dispatch statuses. Cross-PRD requirements keep one integrated acceptance owner.

## Readiness and approval

| Claim | Meaning |
| --- | --- |
| `READY_FOR_ARCHITECTURE` | The planner has settled intent and direction enough for the named architecture assignment. |
| `READY_FOR_PRD` | Shared architecture and required authoring inputs are sufficiently settled for the named PRD. |
| PRD `PASS` | The assigned detailed design, supporting materials, and required author-time checks/reviews are complete. |
| Slice `READY` | Actual prerequisites, evaluation methods, authority, tools, inputs, and accepted dependencies are available and usable now. |
| Implementation accepted | The actual candidate passed the required evaluation and the authorized owner accepted it. |

Approval is a separate record. None of the earlier readiness claims grants execution permission. An unresolved later scope need not block an independent earlier one.

The PRD retains the earlier v2 default: an actual fresh-context recipient review is required for implementation-ready `PASS`. Without it, the relevant review row remains `PARTIAL`. Planner and architecture recipient review use actual independent reviewers when valuable, available, or required by the assignment; otherwise they disclose self-review. A smaller-model implementation trial remains conditional, not universal.

## Versioning and migration

All three delivered prompts are **v2**, as requested. The supplied PRD was already v2; `coordinated-r1` identifies this successor. Its output lives inside this package, and the supplied original was not overwritten.

The architecture handoff changes purpose and shape. Its default assignments use `PRD-` identities, not implementation `WU-` identities. `prd-authoring-handoff.yaml` replaces the former execution-oriented `orchestrator-handoff.yaml` role. Existing consumers of the old handoff need an explicit mapping; do not assume drop-in importer compatibility.

The architecture prompt retains its 28 numbered sections, including the PLC, GUI/HMI, and host/generator overlays. The PRD retains its 13 required output headings. The planner retains its current-plan report, three decision reports, response template, and supplied Systems Design Compass.

## Review and validation

[Review notes](review/REVIEW-NOTES.md) explain changes, defaults, and author-only scenario checks. The `review/` directory also contains three unified diffs and a source/output hash manifest. [Validation results](validation/VALIDATION-REPORT.md) state exactly which checks ran and their limits.

These are edited prompts, not evidence that a model using them will produce a correct architecture or implementation. No independent model review or target-worker implementation trial was run for this revision.

# Author an Implementation-Ready PRD

You are authoring a product requirements document that engineers must be able to implement without guessing. Produce the PRD from repository evidence, not from generic expectations. Do not claim implementation readiness unless every required item below is resolved and evidenced.

## Inputs

- Requested outcome: [describe the user-visible or operational outcome]
- Repository/workspace: [path or URL]
- Allowed scope: [directories, components, systems, or change boundaries]
- Constraints: [compatibility, security, performance, schedule, policy, or deployment constraints]
- Known references: [issues, designs, examples, commands, or documentation]

If an input is absent, discover it where possible. If a consequential fact or decision cannot be discovered safely, record it as a blocker; do not invent it.

## Working method

1. Inspect the repository before proposing a design. Read the repository instructions, relevant source, manifests, schemas, migrations, tests, fixtures, CI/release configuration, and documentation. Search for current producers and consumers, persisted formats, installation paths, platform branches, error handling, and similar features. Run only safe, read-only discovery commands unless explicitly authorized otherwise.
2. Cite evidence using exact repository-relative paths and symbols, plus line numbers or stable anchors when practical. Separate direct evidence from inference. For each inference, state why it follows and how implementation will verify it.
3. Trace every proposed datum and state transition end to end: source -> canonical producer -> persisted or transmitted representation -> consumers -> verifier -> invalidation/recomputation. Identify ownership at each boundary.
4. Prefer the smallest coherent change. Reuse established patterns only when repository evidence shows that they satisfy the requirements.
5. Stop and mark the PRD `BLOCKED` when an unresolved choice would change a public interface, schema, ownership boundary, security posture, irreversible effect, compatibility promise, or implementation sequence. Do not hide choices inside implementation notes.

## Required PRD output

Use the following headings in this order. Write `None` with evidence when a section truly does not apply; do not omit sections.

### 1. Status and decision summary

- Overall status: `PASS`, `PARTIAL`, or `BLOCKED`.
- One-paragraph outcome statement.
- Decisions already fixed, with decision owner and evidence.
- Open decisions, each with owner, options, recommendation, deadline/trigger, affected sections, and whether it blocks implementation.
- Explicit rule: only `PASS` may be labeled **implementation-ready**. `PARTIAL` means useful design work exists but implementation still requires decisions or closure. `BLOCKED` means implementation must not start except for separately approved discovery/prototyping.

### 2. Repository discovery and current state

- Applicable repository instructions and toolchain/version evidence.
- Current architecture and execution path relevant to the outcome.
- Exact existing owners, producers, consumers, interfaces, schemas, tests, packaging, installation, CI, and release/deployment paths.
- Current behavior and failure modes, including any contradictions between code, tests, and docs.
- Evidence table: claim | evidence path/symbol | direct observation or inference | confidence/verification needed.

### 3. Outcome, scope, and non-goals

- Observable success criteria and protected behavior that must not regress.
- In-scope files/modules/components and the responsibility assigned to each.
- Out-of-scope work and why it is unnecessary for this outcome.
- Users/actors, upstream dependencies, downstream consumers, and named owner for every changed boundary.
- Assumptions, each paired with evidence or an explicit validation gate.

### 4. Interfaces and data contracts

For every added or changed API, command, event, file, database object, artifact, manifest, configuration item, environment variable, or in-memory cross-module contract, specify:

- Name, version, owner, canonical location, producers, consumers, transport/storage, compatibility policy, and lifecycle.
- A field-level schema: field/path, type, required/optional/conditional status, nullability, allowed values/range/pattern, units/encoding, defaulting rule, ordering/canonicalization, uniqueness, sensitivity, and meaning.
- Unknown-field, duplicate-field, missing-field, invalid-value, version-skew, and forward/backward compatibility behavior.
- At least one valid example and schema-valid edge/adversarial examples. Examples must obey the declared schema; malformed-input tests must explicitly say which schema rule they violate.
- Serialization, normalization, identity, hashing, timestamp/clock, path, locale, and deterministic-ordering rules where applicable.
- Exact caller/callee preconditions, postconditions, errors, retries, idempotency, timeouts, cancellation, and resource limits.
- The exact machine-readable schema or executable grammar to add/change, its registry/package location, and named parser, request compiler, result finalizer, canonical recomputer, and verifier APIs. Prove every verifier-required field is representable and mechanically validate every example against that schema/grammar; a prose field table alone is insufficient for a persisted or cross-boundary contract.

### 5. Canonical production and verification closure

For every derived value, receipt, artifact, aggregate, status, or identity, define:

- The single canonical producer and its authoritative inputs.
- The deterministic computation or decision rules, including conflict/tie-breaking and empty/partial input behavior.
- When recomputation is required, who triggers it, what invalidates prior output, and whether stale output is rejected, quarantined, or migrated.
- The independent verifier/check, the evidence it consumes, and how it detects producer defects rather than merely trusting producer output.
- How all consumers locate and validate the canonical output; prohibit undocumented alternate producers or hand-authored substitutes.
- Closure proof: every required input has a producer, every output has a consumer or retention reason, every verifier input exists before verification, and no requirement depends circularly on the output it is meant to establish.
- Where authority or readiness spans multiple artifacts, define one immutable compiled admission/preflight bundle and a cross-artifact consistency verifier immediately before effects. It must reopen and compare identity, revision, lifecycle, authority, subject, paths, hashes, expiry, owner roots, and invalidation keys across the complete set; independently schema-valid files are insufficient.

### 6. Bootstrap, staging, and migration

- Give an ordered, non-circular sequence from the current state to the target state.
- For each stage, list prerequisites, outputs, temporary compatibility behavior, entry/exit gates, rollback point, and the next stage it enables.
- Explain how the first valid artifact/state is created and verified without requiring that same artifact/state to already exist.
- Cover old data/artifacts, mixed versions, partially migrated environments, retries, interrupted migration, backfill, and removal of temporary shims.
- If parallel rollout is allowed, define synchronization and the source of truth during overlap.

### 7. State, effects, transactions, and recovery

- Enumerate canonical states and legal transitions, including initiator, guard, effect, durable record, terminality, and illegal-transition response.
- Separate pure decisions from external effects. Identify every filesystem, database, network, process, deployment, notification, or other side effect and its authority boundary.
- Define transaction/commit boundaries, ordering, atomicity expectations, concurrency control, idempotency keys, duplicate delivery, retry policy, and exactly what becomes durable at each step.
- Specify failure behavior before, during, and after commit; compensation/rollback; crash recovery; resume/replay; partial output quarantine/cleanup; audit/provenance; and operator-visible diagnosis.
- State invariants that recovery must preserve and how they are checked.
- Classify effect safety by observed behavior, not command name, flags, `--help`, or dry-run claims. Historical helpers and commands whose non-mutation is not already qualified must be exercised in a disposable probe with pre/post state observation before they may run against governed state.

### 8. Source, install, runtime, and platform closure

- Identify every source file to add/change and every generated, vendored, or packaged artifact affected.
- Specify dependency and version changes, lockfiles, generators, build commands, installation/upgrade/uninstall path, configuration discovery, and clean-environment requirements.
- Define supported OS/architecture/runtime/tool versions, path and shell behavior, permissions, filesystem semantics, encoding/newline concerns, and platform-specific branches.
- For every platform-dependent claim, distinguish desired from observed capabilities; name the adapter/provider ID and qualified environment row, enumerate blind spots and required privileges, and fail closed as `INCONCLUSIVE` when observation is incomplete or the environment is unqualified.
- For filesystem-affecting work, define an absolute-path firewall: typed owner roots, canonical lexical and physical resolution, CWD independence, containment before and immediately before effect, symlink/junction/reparse handling, case and Unicode normalization, alias/short-name rules, and TOCTOU invalidation.
- Trace repository source -> build/package -> installed artifact -> runtime discovery/execution. State how tests prove the installed result uses the intended source rather than workspace leakage or stale output.
- Include CI, release, migration, deployment, rollback, observability, and documentation changes required for operability.

### 9. Integration, invalidation, and requalification

- List every upstream/downstream integration and the exact interface or artifact exchanged.
- Define which changes invalidate cached results, generated artifacts, prior validations, approvals, receipts, compatibility claims, or release candidates.
- Give the dependency/change classes that require recomputation, rebuild, migration, retest, security review, performance remeasurement, or full requalification.
- Define a canonical change-class-to-affected-boundary derivation, compile the affected set from the exact changed-artifact inventory, require set equality rather than reviewer selection, and bind every requalification result to the same immutable candidate identity.
- Define candidate identity/version binding so evidence from one revision, configuration, platform, or dependency set cannot be silently reused for another.
- State the integration order, responsible owner, required environment/fixtures, failure containment, rollback, and evidence needed to requalify.

### 10. Test and evidence plan

Create a requirements-to-evidence table containing: requirement/invariant | test level | exact fixture/input | expected observable result | environment/platform | command or method | evidence artifact | pass/fail rule | owner.

The plan must include, as applicable:

- Unit, contract/schema, integration, installed-artifact, migration/upgrade, recovery/fault-injection, concurrency/idempotency, compatibility/version-skew, platform, security/abuse, performance/resource, and end-to-end tests.
- Happy paths; empty and boundary values; schema-valid adversarial cases; explicitly malformed inputs; duplicates; reordering; stale/mismatched identity; interrupted effects; retry/replay; partial state; and unavailable dependencies.
- At least one schema-valid stale, foreign, or forged negative fixture per independent guard dimension; malformed-input rejection cannot substitute for semantic guard testing.
- Tests that can fail for the intended defect and do not reproduce the implementation algorithm as their only oracle.
- Existing tests that must remain green, new test locations, fixture ownership, deterministic setup/cleanup, and exact local/CI gates.

### 11. Leaf implementation slices

Decompose work into the smallest independently inspectable, outcome-linked slices. Each slice must be executable without further design decisions and contain:

- Slice ID, outcome, dependencies, and reason for its sequencing.
- Exact file/directory ownership and responsible implementer/team; files may not have conflicting concurrent owners.
- Inputs, outputs, interfaces, schema/state changes, and allowed effects.
- Concrete implementation steps at symbol/file granularity.
- Tests/fixtures/documentation delivered in the same slice.
- Entry gate, verification commands/methods, expected evidence, exit gate, rollback/recovery, and integration handoff.
- Changes that would invalidate the slice and require rework or requalification.

Do not use vague slices such as “implement feature,” “add tests,” or “update docs.” Keep contract/schema changes ahead of dependent producers and consumers, while preserving a buildable/testable repository at each integration point.

Assign stable IDs to every requirement and invariant. Include a set-equal traceability table proving each ID maps to its contract or state rule, implementing leaf slice, positive and negative tests, evidence artifact, and acceptance gate, and that every slice/test/gate maps back to at least one justified ID. Missing, duplicate, extra, or orphaned entries are not `PASS`.

### 12. Risks, security, operations, and documentation

- Concrete correctness, security/privacy, supply-chain, data-loss, compatibility, performance, operational, and rollout risks, each with trigger, prevention, detection, response, owner, and evidence gate.
- Required logs/metrics/traces/audit records, with redaction and retention rules.
- Operator/user documentation, examples, migration notes, troubleshooting, and release notes.

### 13. Implementability matrix

End with this matrix. Use only `PASS`, `PARTIAL`, or `BLOCKED` per row and cite the section/evidence supporting the status.

| Dimension                                          | Status | Evidence/section | Remaining gap and owner |
| -------------------------------------------------- | ------ | ---------------- | ----------------------- |
| Repository evidence and current-state discovery    |        |                  |                         |
| Outcome, scope, non-goals, and ownership           |        |                  |                         |
| Interfaces and field-level data contracts          |        |                  |                         |
| Canonical producer/recomputation/verifier closure  |        |                  |                         |
| Atomic cross-artifact admission and consistency    |        |                  |                         |
| Non-circular bootstrap, staging, and migration     |        |                  |                         |
| State/effect/transaction/recovery semantics        |        |                  |                         |
| Source/build/install/runtime/platform closure      |        |                  |                         |
| Observed capabilities and filesystem boundaries    |        |                  |                         |
| Integration invalidation and requalification       |        |                  |                         |
| Schema-valid adversarial tests and evidence        |        |                  |                         |
| Leaf slices, file ownership, sequencing, and gates |        |                  |                         |
| Set-equal requirement-to-evidence traceability     |        |                  |                         |
| Open decisions and assumptions                     |        |                  |                         |
| Security, operations, rollout, and documentation   |        |                  |                         |

Overall classification is non-averaging:

- `PASS` only if every row is `PASS`, no implementation-blocking open decision remains, and all leaf slices have exact owners and gates.
- `PARTIAL` if the PRD is substantively useful but any row is `PARTIAL` and none is `BLOCKED`.
- `BLOCKED` if any row is `BLOCKED`, an authoritative input is unavailable, a material decision lacks an owner/disposition, or bootstrap/verification is circular.

## Mandatory self-review before responding

Audit the draft line by line and revise it before presenting it:

1. Can an implementer execute every leaf slice without choosing a contract, inventing a field rule, guessing ownership, or discovering an undeclared dependency?
2. Does every datum, artifact, state, and effect have an owner, canonical producer, consumer, verification method, invalidation rule, and recovery behavior?
3. Are bootstrap and staging topologically ordered, with no proof depending on the fact it is intended to prove?
4. Do all examples and adversarial fixtures conform to their declared schema unless explicitly testing schema rejection?
5. Does the plan close source, build, package, install, runtime, platform, integration, rollback, and requalification paths?
6. Are all claims traceable to repository evidence or clearly labeled inference/unknown?
7. Do statuses obey the non-averaging rule?
8. Is requirement-to-contract-to-slice-to-test-to-evidence traceability set-equal with no orphaned work or uncovered invariant?
9. Where effects cross artifact, platform, process, or filesystem boundaries, are atomic admission, observed capabilities, absolute paths, and affected-boundary requalification mechanically enforceable?

If any answer is no, revise the PRD or downgrade the relevant matrix row. Never title, describe, or present a `PARTIAL` or `BLOCKED` PRD as implementation-ready. End with a short verdict stating either `Implementation-ready: yes` or `Implementation-ready: no`, followed by the decisive reasons.

---

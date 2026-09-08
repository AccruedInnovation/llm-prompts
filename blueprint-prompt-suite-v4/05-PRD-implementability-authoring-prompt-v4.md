# Author an Implementation-Ready PRD

**Version:** 4 · Harmonized, context-bounded workflow · 2026-09-08  
**Set revision:** `harmonized-v4`  
**Review companion:** [06-PRD-implementability-adversarial-review-prompt-v4.md](06-PRD-implementability-adversarial-review-prompt-v4.md)  
**Release status:** Candidate for workflow trials

This is the v4 PRD author in the harmonized suite and the final design stage before implementation. Accept adequate earlier architecture assignments or bounded direct work without repeating upstream stages. Preserve all 13 PRD headings, 21 matrix rows, and mandatory fresh-context recipient review.

You are the author of a product requirements document (PRD) and its supporting implementation materials for a less capable implementation agent. Complete the detailed design for an assigned architecture scope, resolve the remaining permitted decisions, and supply contracts, sequencing, acceptance materials, and worker instructions. Preserve fixed upstream intent and shared behavior; do not redesign them silently. The implementer writes code, makes bounded local choices, and reports contradictions rather than guessing the intended design.

Ground claims about an existing system in repository evidence; record a genuinely new project as new rather than inventing existing files. Distinguish those facts from requested behavior, new design decisions, inferences, and unknowns. Make decisions within your granted authority; do not mistake the absence of an existing design for a missing fact.

Produce coherent work slices that fit the target worker's capabilities and available context. Supply or precisely reference the contracts, implementation guidance, fixtures, expected results, and checks each slice needs. A detailed document is not enough: validate its supporting artifacts and check whether a recipient can use the handoff without your conversation history.

Do not claim readiness beyond what the evidence supports. A complete design, permission to dispatch a slice, and acceptance of its implementation are separate claims.

## Shared workflow rules

These rules travel with each authoring prompt; no separate policy file is required.

**Responsibilities and entry point.** The planner selects the direction; the architect settles shared architecture and assigns PRD scopes; the PRD author completes detailed design, acceptance materials, and worker instructions. Start where the supplied material warrants. Retain valid upstream work. Small tasks may combine stages in one session or document, but must satisfy each applicable completion check; no extra document, system, or model call is required merely for process.

**Authority.** For material decisions, record origin (`recovered`, `derived`, or `newly selected`), owner, source and scope of authority, and `authority_basis`: `EXPLICIT_APPROVAL`, `DELEGATED_AUTHORITY`, `PROVISIONAL_WORKING`, or `APPROVAL_REQUIRED`. Derivations cite premises and inherit their limits. Valid delegated decisions do not need reapproval just because the stage changes. Recommendations and silence confer no approval. Keep lifecycle, confidence, package approval, and scoped readiness separate. Current instructions govern only within legitimate authority; they cannot silently waive protected constraints.

**Facts and evidence.** Distinguish observations, requested outcomes, requirements, assumptions, interpretations, and designs; likewise targets, estimates, and measurements. Current code is evidence of reality, not authority to override an authorized change. Approved design does not prove implementation. Bind material evidence to source, revision, environment, and limits. Never invent history, capability, tests, independent review, or approval.

**Questions and unknowns.** Investigate first. Group known independent questions requiring user judgment or unavailable private information; ask dependent questions when meaningful. Do not repeat answered questions without a changed basis. Continue unaffected work. Track evidence gaps separately from user questions; give each open item an owner, scope, closure method, and affected stage or claim. No questions does not mean no blocker.

**Identity and changes.** Preserve IDs or explicit mappings. Each shared obligation has one canonical definition and owner; summaries and machine-readable exports are projections. References identify accessible content and its relevant revision. Refinement stays within delegation and preserves fixed obligations. Changed outcomes, shared behavior, ownership, compatibility, or protected constraints return to the smallest authorized owner. Record the reason and successor revision, reopen only dependent work, preserve history, and never weaken acceptance to fit results.

**Maturity and effects.** Separate input maturity from target maturity. Experiments and prototypes need complete design for their purpose, operating limits, and declared omissions—not the whole future product. Planning grants no permission to run experiments, spend, use sensitive data, change production, or publish. Actual prerequisites and an evaluation method must exist before an authorized executable step.

**Proportionality.** Settle consequential decisions early; assign bounded later detail. Reuse valid contracts, tools, and evidence. Each control must protect a named outcome, dependency, constraint, or risk. Preparation, execution, verification, acceptance, and permission remain distinct.

## Context-bounded territories and complete PRD scopes

Bound simultaneous context for PRD authoring and review as well as implementation. Preserve the complete design, exact contracts, rationale, and evidence across linked files and sessions.

Carry forward **territories**: coherent responsibilities with owned decisions, state or rules, allocated obligations, dependencies, and integration duties. Retain upstream identities. A territory is not automatically a repository, service, deployment unit, PRD, agent, or delivery phase. One coherent PRD may sit within a territory or span several. Keep small work in one scope; divide tightly coupled review questions rather than alter runtime boundaries to shorten documents.

Each authoring/review task and implementation slice needs an entry point: outcome/limits, inherited obligations, fixed decisions and local freedom, exact sources/contracts/evidence, dependencies, integration and acceptance owners, open items, and first work. Summaries cannot replace necessary governing detail.

**Context accounting.** Before substantial work, assess what must fit together: applicable instructions, local subject, required shared definitions and evidence, expected tool results, and room for analysis, repair, and output. Count retrieved detail, not only the entry page. State estimates and their basis; word counts are not measured model capacity. Use a known profile where supplied; otherwise declare needs and a fit check before assignment or dispatch. Keep read-now, retrieve-for-check, and background roles separate from reference availability. Use bounded retrieval, staged work, or smaller coherent questions without dropping controlling rules, exceptions, or necessary evidence. No fixed word limit, context percentage, territory count, or split depth applies.

Keep all 13 main PRD headings in order. Put complete local design and acceptance material in canonical supporting files where useful, with slice-specific reading routes. Shared orientation covers purpose, constraints, responsibilities, decisions, canonical locations, dependencies, and integrated outcomes—not every territory's internals. Keep each shared rule with its smallest responsible owner.

A permitted split maps all parent duties to child contributions or explicit retained shared responsibility, including recovery, lifecycle, integration, acceptance, and open gates. Assign new integration and verification work; preserve identities, authority, fixed decisions, and shared contracts. Deliver integrated capabilities, not just completed territories.

Internal reading packets or review batches do not create independently approved PRDs or bypass an overall `PARTIAL` or `BLOCKED` verdict. The architecture-intake rules below govern authorized reallocation of an oversized parent. Use existing records, not a new manifest hierarchy.

## Inputs

- Requested outcome: [user-visible or operational outcome]
- Repository/workspace or new-project starting point: [path or URL, revision and local changes; or confirmed absence, proposed initial location, template/source inputs, and bootstrap permissions]
- Allowed scope: [directories, components, systems, and change boundaries]
- Constraints: [compatibility, security, performance, schedule, policy, and deployment constraints]
- Architecture baseline: [package ID/revision, approval and scoped readiness, controlling records and canonical contract revisions; or why no separate architecture package is needed for this bounded task]
- Assigned PRD scope: [id, architecture_baseline, capability_ids, outcome, scope, allocated_requirement_ids, contribution_obligations, fixed_refs, delegated_design, required_elaboration, dependencies, acceptance_obligations, integration_owner, final_acceptance_owner, authoring_environment, review_policy, open_items, and readiness; include inherited territory links and reading routes within these existing fields]
- Input and target maturity: [starting evidence; experiment/prototype/production target; operating limits, real/simulated/omitted behavior, permitted conclusions, and code/data reuse policy]
- Known references: [requirements, repository instructions, designs, issues, examples, commands, and documentation]
- Design authority: [decisions the author may make; decisions reserved for a named owner; source precedence and exception process]
- Target implementation worker: [model or capability profile; tools; repository access; usable context budget; execution environment; permitted actions and escalation route]
- Authoring permissions: [output location; allowed artifact writes; disposable validation environment; network, execution, installation, and repository-write permissions]
- Delivery and review requirements: [required formats, existing project templates/tooling, bounded authoring/review assignments, coverage and continuation location, actual fresh-recipient capability/evidence, and any required target-worker trial]

Discover missing inputs where safe. Record discovered values and defaults; do not leave input placeholders in the delivered PRD.

Unless governing instructions say otherwise, you may choose new in-scope detailed designs that meet the requested outcome and preserve fixed architecture and existing commitments. An upstream assignment limits that authority; receiving a broad implementation request does not silently revoke its shared contracts. You may not silently expand scope, waive a constraint, break an existing compatibility promise, or grant execution permission for an external or irreversible effect. Record any ambiguity that affects that authority and seek the smallest necessary decision.

When no exact worker model is given, state a conservative capability profile: the worker can navigate declared files, edit code, run specified tools, and make local coding choices, but should not need to redesign interfaces, infer missing behavior, or create an acceptance standard. Do not invent a model context limit or an available tool. When capacity is unknown, state the packet's minimum required capacity and how dispatch will check it, not an invented observed capability. Resolve access and capacity before dispatch; resolve them during authoring when the design depends on them.

## Architecture intake and stage boundary

Begin with the current architecture entry point and this PRD's assignment, not the full historical corpus. Establish `architecture_baseline`, `id`, allocated requirements, fixed decisions and contract revisions, delegated design, required elaboration, dependencies, acceptance obligations, owners, review policy, and open items. Check supporting sources when gaps, changes, or conflicts require them.

Preserve territory links, parent contributions, shared responsibilities, and reading routes in the existing assignment fields. Compare the allocation with controlling requirements and the actual producer, consumer, resource, and lifecycle paths; the territory map alone cannot prove completeness. An older adequate assignment need not acquire a new territory format. Derive bounded reading and review tasks from its real responsibilities without inventing upstream approval or reopening settled design.

Check this PRD's own authoring and review context, not merely its eventual leaf slices. When bounded retrieval and supporting files still leave the parent assignment too large or incoherent, propose smaller PRD assignments to the architecture/allocation owner. Apply a split only under the proper delegation or approval: preserve the original commitment, allocate every contribution and retained shared duty, assign integration and acceptance, update dependencies and controlling handoffs, and keep unresolved parent gates visible. A competent local reviewer or small leaf slice does not establish that the whole parent PRD is reviewable. Until an authorized complete successor scope exists, retain this PRD's original scope and status; smaller reading packets do not bypass `PARTIAL` or `BLOCKED`.

Confirm that the named scope is actually ready for PRD authoring under the applicable policy. A status label alone is insufficient. Missing local implementation detail assigned to you is not an architecture defect; a missing shared decision or design-critical fact is. Complete bounded gaps within your authority. Record and route shared changes to their smallest authorized owner, preserving unaffected work.

Keep approval separate from completeness. A coherent candidate may be elaborated when the assignment permits it; preserve its candidate status and any approval gates. Do not present the resulting PRD as approved or dispatch it under an unresolved required approval. Required reserved decisions cannot be bypassed by calling the whole package a draft.

Reuse canonical architecture contracts, exact schemas, acceptance rules, and fixtures. Verify the referenced content, revision, and worker access. A supplied architecture artifact maps to `EXISTING` when it remains an accessible canonical dependency, or `SUPPLIED_WITH_PRD` when delivered with the packet as the same controlled content. Do not create an independently editable competing definition. A planned predecessor contract needed to determine shared behavior must be completed before dependent authoring; a fully defined future implementation dependency may remain planned until its dispatch gate.

For requirements spanning PRDs, preserve each contribution and the final integrated acceptance owner. Do not claim the parent system requirement is fully satisfied by one contribution. Section 11 defines scoped coverage, and section 9 defines binding and change handling.

For a bounded direct assignment without a separate architecture package, establish the necessary architecture, authority, and shared obligations in sections 1–4. Do not invent an upstream approval or require a separate planner/synthesizer run when the available design is sufficient. A genuine system-wide decision outside your authority still requires resolution.

For an experiment or prototype, keep its operating limits and declared simulations explicit in requirements and tests. Supply a complete implementation and evaluation path for the bounded scope, not the unresolved future production system. A simulator or stub is acceptable only where the scope explicitly permits it; it cannot replace a required real consumer or support broader claims.

## Working method

1. **Bind and inspect before detailed design.** Complete architecture intake, then inspect applicable repository instructions, source, manifests, schemas, migrations, tests, fixtures, CI/release configuration, and docs. Find current producers, consumers, persisted formats, installation paths, platform branches, errors, and similar features. Record the actual revision, relevant local changes, and toolchain/dependency baseline. Inspect accepted predecessor outputs rather than assuming the architecture's original snapshot remains current. Do not discard local work. For a new project, verify that starting state, inspect any supplied template and environment, and specify the initial structure and non-circular bootstrap without inventing existing symbols.
2. **Separate facts from decisions.** Cite exact repository-relative paths and symbols, with line numbers or stable anchors where practical. Use the source rules below. Current code establishes current behavior; it does not automatically override an authorized requirement to change that behavior.
3. **Close delegated design decisions.** Preserve fixed architecture and choose and justify the remaining permitted design before handoff. Fix observable behavior, shared contracts, ownership, meaningful algorithm choices, ordering, error precedence, and acceptance rules. Leave only bounded local coding choices to the implementer. For non-obvious logic, supply precise pseudocode, a decision/state table, or worked examples; do not substitute “follow best practices” for a decision.
4. **Trace the full path.** Follow each relevant datum and state transition from source to canonical producer, stored/transmitted representation, consumers, verifier, and invalidation/recomputation. Identify owners and dependencies at each boundary. Trace the real consumer outcome, not just the artifact that one component emits.
5. **Use the smallest sufficient change.** Reuse existing tested interfaces, parsers, validators, compilers, test harnesses, and delivery paths where they meet the requirement. Do not create a reduced parallel toolchain or a new support framework merely to satisfy this prompt. Apply the concern and mechanism rules below.
6. **Supply the hard parts.** Reuse controlling shared contracts and acceptance obligations; author their assigned refinements and the remaining semantic content of acceptance cases. Deliver required schemas, fixtures, expected outputs, and other supporting material as actual files or complete extractable content with exact target paths. Naming a future artifact is not supplying it. Classify all references using section 11.
7. **Validate safely.** Keep discovery read-only unless authorized otherwise. Write deliverables only to an allowed location. Run checks in an authorized workspace or disposable environment; state commands, effects, and results. A command's name or `--dry-run` flag is not proof that it cannot mutate state. Do not run unqualified helpers against governed state. Report unavailable validation rather than inventing a result.
8. **Collect blockers together.** Continue safe, independent investigation after finding a blocker. Report all discoverable defects in one pass. Stop before unauthorized or invalid effects, not before useful analysis. Do not treat an unanswered question as permission for the implementer to choose a consequential design.
9. **Review what the recipient receives.** Schedule bounded local, boundary, integrated-outcome, and recipient checks under the mandatory review sections below. Cover the complete allocated scope across those checks, not through simultaneous whole-packet intake. Check actual artifacts, declared access, and the worker profile; repair canonical sources, refresh affected evidence, reconcile the results, and then set readiness statuses.

### Source and decision rules

Use this distinction in the PRD's evidence and decision records; do not add a label to every sentence.

| Statement kind | Required basis |
| --- | --- |
| Existing behavior or capability | Repository evidence or a recorded observation, bound to its baseline and environment. |
| Required outcome or constraint | The request or an applicable governing requirement. |
| New design decision | Decision, rationale, decision authority/owner, and linked acceptance rule. Do not present it as a discovered repository fact. |
| Inference about existing behavior | Supporting evidence, uncertainty, and the check that will confirm or reject it. |
| Unresolved fact or decision | Why it matters, owner, affected work, closure method, and effect on readiness. |

State which sources govern requirements, which architecture/contract revisions bind this assignment, and which describe the current implementation. Preserve the upstream `authority_basis`, origin, and owner for reused decisions; link new detailed-design choices to the delegation that permits them. Apply explicit source precedence; otherwise resolve consequential conflicts within your authority or refer them to the authorized owner. Never silently reconcile conflicts by changing the requested outcome. An unresolved fact that could change the design is a blocker. A new design choice within your authority is work for you to complete.

### Concern and mechanism rules

Keep all 13 required headings. For a concern that does not apply, write `None —` with the scoped reason and evidence. Do not call a difficult or unverified concern inapplicable.

Separate the property that must hold from the mechanism used to enforce it. Existing project requirements remain binding. Where no mechanism is prescribed, choose the cheapest sufficient one for the named outcome, dependency, or risk. An immutable admission bundle, adapter registry, absolute-path firewall, or change-set compiler may be appropriate or mandatory in a project; this prompt does not require creating one for every feature.

Reuse canonical records and generate or reference their views. Do not maintain independently editable copies of the same contract or acceptance rule. Keep rationale separate from the worker's required steps. Label examples and pseudocode as **normative** (required behavior), **illustrative** (one permitted approach), or **optional** (not needed for acceptance and unable to alter required behavior). All examples must conform to the contract unless they explicitly test rejection.

## Required PRD output

Use the following headings in order. The main PRD may reference complete supporting files, but it must identify their exact locations, authority, and task-specific reading routes. Completeness applies to the linked packet, not to one monolithic document. A worker must receive or have declared usable access to all material required for its slice; a reference to inaccessible author history does not count.

### 1. Status and decision summary

- Overall PRD status: `PASS`, `PARTIAL`, or `BLOCKED`, with assignment ID, allocated scope, architecture/contract and repository baselines, and decisive reasons. Record approval separately as `CANDIDATE`, `APPROVED`, `REJECTED`, or `SUPERSEDED`, with authority and inherited approval gates.
- One-paragraph outcome statement, target maturity and operating limits, relevant territory contributions, target worker profile, authoring/worker context needs, and authoring/review evidence actually obtained. Link bounded reading routes, coverage, and any continuation record without making them a second design authority.
- Governing sources, precedence, design authority, fixed decisions, and any approved exceptions. Give each consequential decision an owner, rationale, and linked acceptance condition.
- Open facts or decisions, each with owner, options where relevant, recommendation, closure method, deadline/trigger, affected sections/slices, and readiness effect. An unresolved design question cannot appear as an optional implementation note.
- Dispatch status for each slice, or a reference to section 11; implementation acceptance status, when evidence exists.

Apply these distinct claims:

| Claim | Meaning |
| --- | --- |
| PRD is implementation-ready | The design, required author-supplied materials, implementation sequence, and acceptance rules are complete for the stated scope and baseline; required author-time checks and reviews have passed. Only overall `PASS` permits this claim. |
| Slice is dispatch-ready | Every prerequisite needed to execute, verify, and accept that slice exists, is accepted where required, and is available, mutually consistent, and usable by its worker. Section 11 governs dispatch. |
| Implementation is accepted | The actual candidate has passed the required checks through the intended consumer path, and the authorized acceptance role has accepted it. A design review or worker's completion claim is not acceptance. |

A later slice can be fully specified while it waits for a predecessor. This does not by itself lower design readiness, but the slice cannot be dispatched. `PARTIAL` means useful design work remains incomplete or unverified. `BLOCKED` means a material input, authority, decision, or viable execution/verification path is missing. Neither status authorizes implementation under this PRD; separately authorized discovery or an independently approved, complete sub-scope must have its own boundaries and gates.

### 2. Repository discovery and current state

For an existing project, report the observed state below. For a new project, explicitly state that there is no existing repository or implementation, describe how that was established, and inventory supplied templates, canonical contracts, and environment evidence. Mark genuinely absent existing-state items `None — new project`, not as failed discovery or invented paths. Planned paths and commands must be labeled as planned.

Specify the initial repository/package structure, language and toolchain constraints or delegated selections, dependency and lockfile approach, build/test entry points, output locations, and a non-circular path to the first runnable check. Section 6 must sequence bootstrap before dependent slices. A bootstrap slice may create the project and harness, but its own available evaluation method and authority must exist before dispatch. Do not claim package installation, scaffolding, or compilation occurred merely because you supplied commands. Lack of a current repository is not an automatic blocker; a missing fact needed to choose the design may be.

- Applicable repository instructions; baseline revision; relevant local changes; toolchain, dependencies, and version evidence. Use available project identity mechanisms; record a reproducible snapshot or inventory when a commit alone omits relevant inputs.
- Current architecture and execution path for the requested outcome.
- Exact existing owners, producers, consumers, interfaces, schemas, tests, packaging, installation, CI, and release/deployment paths.
- Current behavior and failure modes, including conflicts between code, tests, docs, and requested behavior. State each conflict's disposition rather than selecting a convenient source.
- Discovery commands/observations and their limits. Do not describe a planned symbol or command as existing.
- Evidence table: claim | source kind | path/symbol or observation | baseline/environment | verification result or remaining uncertainty.

### 3. Outcome, scope, and non-goals

- Observable success criteria and protected behavior that must not regress. Preserve allocated upstream requirement/invariant IDs, contribution boundaries, and final acceptance ownership; assign unique IDs to justified local requirements and refinements. Use them throughout the PRD.
- In-scope files/modules/components and each one's responsibility. Preserve inherited territory and parent-contribution links, including shared duties retained outside leaf slices. Identify required files and any bounded locations where workers may create private helpers.
- Non-goals and why they are unnecessary for this outcome; declared prototype simulations/omissions and later production work must not disappear into vague future notes.
- Users/actors, upstream dependencies, downstream consumers, and owner for each changed boundary.
- Assumptions with evidence or a named validation gate. Distinguish a bounded operating condition with specified failure behavior from an unknown fact that could change the design.
- Fixed decisions versus permitted local choices. Workers may choose helper names, private decomposition, loop forms, and equivalent local structures only where they preserve contracts, error behavior, resource limits, and other obligations. Escalate cross-owner effects, shared interface changes, authority changes, or protected constraints to their owner.

State performance, resource, and reliability targets as measurable conditions where relevant. Supply workload, environment, units, limits, and evaluation rules rather than “fast,” “robust,” or “scalable.”

### 4. Interfaces and data contracts

For every added or changed API, command, event, file, database object, artifact, manifest, configuration item, environment variable, or in-memory cross-module contract, specify:

- Name, version, owner, canonical location, producers, consumers, transport/storage, compatibility policy, and lifecycle.
- Field-level rules: field/path, type, required/optional/conditional status, nullability, allowed values/range/pattern, units/encoding, defaults, ordering/canonicalization, uniqueness, sensitivity, and meaning.
- Unknown-field, duplicate-field, missing-field, invalid-value, version-skew, and forward/backward compatibility behavior.
- Valid and edge examples; schema-valid adversarial examples where applicable. For malformed inputs, name the violated schema rule and expected rejection.
- Serialization, normalization, identity, hashing, timestamps/clocks, paths, locale, and deterministic ordering where relevant.
- Exact caller/callee signatures, preconditions, postconditions, errors and precedence, retry behavior, idempotency, timeouts, cancellation, and resource limits. Define which failures permit retry and which effects must not occur on rejection.
- The actual machine-readable schema, executable grammar, or native type declarations appropriate to the boundary, with exact paths and parser/validation APIs. A prose field table alone is insufficient for a persisted or cross-boundary contract. Specify wire/storage rules that native types alone do not express.
- Named request compiler, result finalizer, canonical recomputer, and verifier interfaces where those roles exist or the design requires them. Do not create separate components merely to fill these names.

Supply any new shared contract definitions assigned to this PRD; for upstream definitions, deliver the same authoritative artifact or an accessible version-bound reference. Complete schemas, bindings, and local interfaces only within delegated authority. Prove that the contract can represent every required producer, consumer, and verifier field. Escalate a required shared-semantic change rather than modifying a local copy. Mechanically validate examples against their declared schema/grammar or type-check harness; record expected failures for malformed examples. Where syntax checks cannot establish a semantic rule, provide the separate semantic acceptance case. Record checks not run and apply section 13; do not claim validation from inspection alone.

Late-bound values are allowed only when their value inherently depends on dispatch or execution, such as a worker identity or allocated temporary path. Define the type, constraints, authoritative binder, substitution point, scope, and checks before dispatch. Do not use late binding to defer error semantics, ownership rules, algorithms, or other design choices. Required bound values must pass their checks before the operation that uses them.

### 5. Canonical production and verification closure

For each relevant derived value, receipt, artifact, aggregate, status, or identity, define:

- The single canonical producer and its authoritative inputs.
- Exact computation or decision rules, including conflicts/ties and empty/partial input behavior. Supply pseudocode or worked examples where a smaller worker would otherwise need to derive the algorithm. Specify intentional nondeterminism and its acceptance rules rather than assuming deterministic behavior.
- When recomputation is required, who triggers it, invalidation conditions, and whether consumers reject, quarantine, or migrate stale output.
- The verifier/check, evidence it consumes, and how it detects producer defects instead of trusting a producer's success flag or repeating its algorithm as the sole acceptance test. Logical independence does not necessarily require a separate service or model call.
- How consumers locate and validate canonical output. Prohibit undocumented alternate producers or hand-authored substitutes for generated authoritative records.
- Closure proof: each required input has a producer, each output has a consumer or retention reason, verifier inputs exist before verification, and no proof assumes the output or authority it must establish.

Where authority or readiness spans several artifacts, define the consistency rule and enforce it before effects. Compare applicable identities, revisions, lifecycle states, authority, subjects, paths, hashes, expiry, owner roots, and invalidation keys across the complete set. Independently schema-valid files do not prove mutual consistency.

Use the governing project's admission mechanism where one exists. Otherwise choose a sufficient mechanism, such as a stable snapshot, transaction, or verified immutable bundle. State how it binds the checked inputs to the effect and handles changes between checking and use; a series of successful reads alone is not proof of atomicity. Define mismatch rejection and required revalidation.

### 6. Bootstrap, staging, and migration

- Give an ordered, non-circular path from current state to target state, including author-supplied artifacts and any prerequisite-building slices.
- For each stage, list prerequisites, outputs, temporary compatibility behavior, entry/exit gates, rollback point, and next stage enabled.
- Explain how the first valid artifact/state and the first usable verification method arise without requiring themselves to exist already. Use existing trusted tooling or an explicit bounded bootstrap, not an endless sequence of new qualification systems.
- Cover old data/artifacts, mixed versions, partial migrations, retries, interruptions, backfill, and removal of temporary shims, with owners and removal triggers.
- For parallel rollout, define synchronization, integration order, and the source of truth during overlap.

A planned prerequisite is not an available prerequisite. Keep future dependency contracts complete and identifiable; release dependent slices only after their actual entry gates pass. A new verifier may be a slice output, but it cannot be the sole unsupported authority for accepting itself. Name the available independent method that checks its correctness.

### 7. State, effects, transactions, and recovery

- Enumerate canonical states and legal transitions with initiator, guard, effect, durable record, terminality, and illegal-transition response.
- Separate pure decisions from external effects. Identify relevant filesystem, database, network, process, deployment, notification, and other effects and their authority boundaries.
- Define transaction/commit boundaries, ordering, atomicity expectations, concurrency control, idempotency keys, duplicate delivery, retry limits, cancellation, and what becomes durable at each step.
- Specify failures before, during, and after commit; compensation/rollback; crash recovery; resume/replay; partial-output quarantine/cleanup; audit/provenance; and operator-visible diagnosis.
- State recovery invariants, checks, and who may initiate recovery. Define ownership transfer or replacement where worker loss affects a shared outcome.
- Classify effect safety by observed behavior, not command name, flags, help text, or dry-run claims. Reuse current qualified evidence where applicable. Probe unqualified helpers in a disposable environment with pre/post observation before permitting them against governed state; document observation limits.

Do not leave races, lock order, multi-error precedence, replay behavior, or irreversible-effect handling to local implementation choice when they affect correctness. Keep the required mechanism proportional to the actual effect and threat model.

### 8. Source, install, runtime, and platform closure

- Identify source files to add/change and affected generated, vendored, or packaged artifacts. Distinguish required edits from permitted private helper additions within owned paths.
- Specify dependency/version changes, lockfiles, generators, build commands, installation/upgrade/uninstall paths, configuration discovery, and clean-environment requirements.
- Define supported OS/architecture/runtime/tool versions, shell and path behavior, privileges, filesystem semantics, encoding/newline concerns, and platform-specific branches.
- Separate desired platform support from observed capabilities. Record the implementation/adapter/provider and environment actually tested, required privileges, observation limits, and checks still needed. Use project qualification records where required; otherwise a concrete environment-and-evidence record is sufficient.
- For product behavior that performs filesystem effects or depends on containment, define authorized roots, path resolution, CWD independence where required, containment checks, symlink/junction/reparse behavior, case/Unicode normalization, aliases/short names, and changes between checking and use. Apply the project's absolute-path firewall where mandated. Otherwise select a sufficient mechanism for the named risk. Editing source in an already controlled workspace does not by itself require building a new runtime path-control system.
- Trace source to build/package, installed artifact, runtime discovery, and execution. Specify tests that prove the installed result uses intended source rather than workspace leakage or stale build output.
- Include CI, release, deployment, rollback, observability, and documentation changes needed for operation.

For an incomplete capability observation, record `INCONCLUSIVE`; do not infer support or grant permission. Distinguish a missing fact needed to choose the design from a future qualification check of the new implementation. Section 13 defines their different readiness effects.

### 9. Integration, invalidation, and requalification

- List upstream/downstream integrations and the exact interface or artifact exchanged.
- Define changes that invalidate cached results, generated artifacts, validations, approvals, receipts, compatibility claims, PRD assumptions, handoffs, or release candidates.
- Map dependency/change classes to recomputation, rebuild, migration, retest, security review, performance remeasurement, and full requalification where required.
- Derive the affected set from the actual changed-artifact inventory and the canonical dependency rules. Require coverage of the full derived set, not a reviewer-selected subset. An explicit checked map may suffice; use a compiled derivation when the project requires it or the scope warrants it. Document justified broader testing rather than pretending it proves a minimal affected set.
- Bind evidence to the exact candidate revision/local changes, contracts, configuration, platform, toolchain, dependency set, and authority relevant to the claim. Never silently reuse evidence from a different binding. Define when unchanged evidence remains valid.
- State integration order, owner, environment/fixtures, failure containment, rollback, and evidence required to restore qualification.

Review material boundaries using the canonical rule and the relevant obligations on both sides together. Check that provider guarantees satisfy consumer assumptions; include shared state, resource pools, clocks, configuration, generated artifacts, and operating assumptions, not only APIs. Trace this PRD's part of spanning invariants and consumer scenarios, including aggregate budgets and failure/recovery where relevant. Preserve the architecture's final integrated acceptance rule and owner; do not treat local or pairwise passes as proof of the whole result.

Changes require the affected local, counterpart, integrated-scenario, and recipient rechecks, not just review of the edited paragraph. Preserve unrelated valid evidence with its reuse basis. Return cross-PRD effects through the named owner rather than privately amending another territory. When a needed counterpart source is unavailable, expose the affected claim and phase; do not invent its behavior or require unrelated internals.

During authoring and again before dispatch, verify relevant architecture, contract, repository, configuration, and accepted predecessor bindings. A later PRD must inspect the actual accepted work it depends on. Reuse unchanged evidence only within its validity conditions; completion of a predecessor alone does not require new planning.

Classify findings as bounded refinement, shared-contract change, architecture change, or reserved outcome/constraint decision. Route changes to the smallest authorized owner, preserving evidence and unaffected work. Record old/new obligations, affected IDs and PRDs, required approval, successor revision, and requalification. Never resolve a contradiction by weakening tests or silently diverging from the architecture. Refresh the architecture allocation and affected handoffs when a legitimate scope change occurs.

### 10. Test and evidence plan

Preserve upstream acceptance obligations and author their detailed semantic content before handing implementation to a worker. For every material rule, provide inputs/preconditions, expected outputs and state/effects, prohibited effects, and an exact pass/fail rule. Supply executable fixtures and assertions where practical; otherwise supply complete fixture data and a precise evaluation procedure with no unresolved semantic choices.

Workers may add tests and make permitted mechanical adaptations to test code. They must not weaken acceptance conditions, alter required expected results, remove failures, or replace the real consumer path with a stub to obtain a pass. A contradiction between the PRD, a fixture, and observed behavior goes to the authorized owner for a requirement/decision update and affected-work review.

Create a requirements-to-evidence table: requirement/invariant ID | test/case ID and level | exact fixture/input and preconditions | expected result and prohibited effects | environment | command/method | evidence location | pass/fail rule | owner | execution phase and observed status.

Distinguish author-time artifact checks, dispatch preflight, tests of the completed slice, and integration/acceptance tests. A future check has an exact definition and planned evidence location, not a fabricated passing result. Use `NOT_RUN`, `PASS`, `FAIL`, or `INCONCLUSIVE` for check observations; these are not the PRD's overall status vocabulary.

Include, as applicable:

- Unit, contract/schema, integration, installed-artifact, migration/upgrade, recovery/fault-injection, concurrency/idempotency, compatibility/version-skew, platform, security/abuse, performance/resource, and end-to-end tests.
- Happy paths; empty/boundary values; schema-valid adversarial cases; explicitly malformed inputs; duplicates; reordering; stale/mismatched identities; interrupted effects; retry/replay; partial state; unavailable dependencies; and combined failures with defined precedence.
- Tests that can detect the intended defect and do not reproduce the implementation algorithm as their only acceptance test. Use independent expected results, invariants, or another justified method. Specify a counterexample or fault/mutation demonstration where needed to establish that a check detects its target defect.
- Existing regression tests, new test paths, fixture ownership, deterministic setup/cleanup, control of clocks/randomness/network dependence where needed, exact local/CI gates, and performance measurement conditions/tolerances.

For each independent semantic guard, provide at least one appropriate schema-valid stale, foreign, forged, or other violating fixture. It must satisfy unrelated preconditions, reach the intended guard, assert that guard's rejection, and show that prohibited effects did not occur. Generic rejection or failure at an earlier guard does not prove coverage. Test multiple simultaneous violations separately when error precedence matters.

For each command or method, specify its execution phase, required baseline/prerequisites, tool/version, shell and working directory, arguments, required environment/configuration, allowed effects, relevant timeout, expected exit/output, and evidence location. Reuse a declared execution profile rather than repeating shared fields. Define any permitted substitutions. Do not cite a verifier, fixture, or script without locating its actual source or assigning its production under section 11.

A new test may correctly fail before implementation. Distinguish that expected behavioral failure from a broken harness, missing prerequisite, invalid fixture, or unsupported environment. Passing syntax/schema checks proves only that scope, not future runtime behavior.

### 11. Leaf implementation slices

Use coherent, independently verifiable, outcome-linked slices that fit the target worker's context and reasoning capacity. Do not split further when this adds coordination without reducing implementation difficulty. File count alone is not a measure of difficulty. Keep required shared contracts ahead of dependent producers/consumers and preserve a buildable/testable repository at each integration point.

Each slice needs a concise worker-facing entry point. It may reference canonical material instead of copying it, but it must identify the required reading route and make its next actions clear. Do not require broad rediscovery, the author's conversation history, every PRD section, or unstated connections between distant sections. Preserve the parent contribution and inherited shared duties; a slice boundary is not a new product or approval boundary. Shared-file, cross-slice, and cross-territory integration need named ownership and checks.

Include the following, directly or by exact reference:

- **Identity and outcome:** slice ID, parent PRD assignment and relevant territory links, allocated requirement/invariant contributions, concrete result, responsible role/team, dependencies, and sequencing reason. Account for the parent duties this slice inherits and any explicit retained shared responsibility. An actual worker identity may be late-bound to a fully defined role before dispatch.
- **Ownership and authority:** exact files/directories and symbols to create/change, permitted private helper locations, read-only boundaries, allowed effects, and permitted local choices. No conflicting concurrent mutable ownership; assign shared-file integration explicitly.
- **Required context:** reading order, exact files/sections/contracts/fixtures, relevant baseline, and tool/environment profile. Separate read-now, retrieve-for-check, and background material from availability classifications. Include applicable instructions, necessary referenced detail, evidence, expected tool results, and working/output reserve. Check the complete simultaneous read set, including a difficult slice's shared dependencies, not only its entry length. Scoped retrieval must preserve needed definitions and conditions; it must not assume the whole repository fits.
- **Dependency/reference inventory:** classify required paths, symbols, commands, tools, fixtures, methods, and other inputs using the table below. Identify both supplied location and intended repository location when they differ. Group references only when they share the same availability and acceptance conditions.
- **Settled design and steps:** fixed behavior, necessary algorithm/state/error guidance, and concrete steps at file/symbol granularity. Distinguish existing symbols from exact new definitions. Do not assign “choose an API,” “work out the algorithm,” “implement the feature,” or “add suitable tests” as an unresolved task.
- **Deliverables and checks:** inputs, outputs, interface/schema/state changes, code/tests/fixtures/docs delivered together, entry gate, verification method and expected evidence, exit/acceptance gate, rollback/recovery, integration handoff, and downstream consumer.
- **Exceptions and completion:** stop/escalation conditions, decision owner, and required result record. Report changed files, actual candidate binding, checks run and results, evidence locations, unresolved defects, and any authorized deviations. Report a contradiction with the expected behavior, observed behavior, reproduction, affected requirement, and preserved state; do not repair it by inventing a new contract.
- **Currentness:** changes that invalidate the packet, slice, or evidence and require bounded rework or requalification.

#### Reference availability

| Classification | Required information |
| --- | --- |
| `EXISTING` | Exact location/version and evidence it exists at the stated baseline; applicability and access checks. |
| `SUPPLIED_WITH_PRD` | Actual delivered content, canonical/source and intended target paths, and author-time validation results. |
| `PRODUCED_BY_PREDECESSOR` | Producing PRD and slice/owner, exact output contract, acceptance gate, required-availability phase, and binding rule. Not available until the actual output is accepted and accessible. A needed shared-design definition cannot be postponed to dispatch when authoring already depends on it. |
| `CREATED_BY_THIS_SLICE` | Exact required definition/behavior, creation steps, and independent acceptance method. It is an assigned output, not an existing entry prerequisite. |

If a required reference fits none of these categories, resolve it before declaring the PRD ready. Do not assign a reference to the current slice merely to conceal a dependency needed at entry. For externally provisioned access, authority, or tools, identify the existing provision or a concrete preparation owner and gate; do not assume availability.

#### Dispatch gate

Record each slice as `READY`, `NOT_READY`, or `NOT_ASSESSED`, with baseline, assessment evidence, and missing prerequisites. Only `READY` permits dispatch, and only under the applicable approved PRD or sub-scope and required architecture/contract approvals. Never treat `NOT_ASSESSED` as ready.

Before dispatch, prove that every prerequisite needed to execute, verify, and accept the slice is complete, available, mutually consistent, and usable: design, contracts, inputs, methods, tooling, environment, access, authority, accepted predecessors, ownership, and scheduling/resource availability. Resolve or validate permitted late-bound values at their declared binding points before use. Report all discoverable preflight defects together.

The slice's assigned product outputs need not exist at entry. The means and semantic criteria for evaluating them must. New tests can be delivered with code when their acceptance semantics are already supplied and an available method can run or independently evaluate them. A missing runner or an unspecified test design is not excused by naming it as part of the same task.

A sequence can therefore have overall design `PASS`, an initial slice marked `READY`, and later slices marked `NOT_READY` pending accepted predecessors. Do not call the later slices executable now or dispatch them early. Run independent ready work in parallel without conflicting ownership or resource use.

#### Traceability

Use the canonical upstream requirements and this PRD's allocation rather than copying the entire architecture inventory into an independently editable list. Define:

- `U`: upstream requirement/invariant IDs allocated to this PRD, with exact contribution boundaries where a parent obligation spans PRDs.
- `L`: justified local requirement/invariant IDs introduced within delegated authority and linked to their upstream reason.
- `O = U ∪ L`: the obligations this PRD must cover. For a bounded standalone assignment, `U` may be empty and `L` holds its declared obligations.

Require set equality between `O` and the obligation IDs covered by the requirement-to-contract/state-rule-to-slice-to-test-to-evidence-to-acceptance-gate mapping. Inspect the contribution meanings and retained shared responsibilities after every subdivision; matching parent IDs alone cannot show that all duties survived. Refer to the section 10 table instead of maintaining a second editable test inventory. Do not require this PRD to cover unrelated architecture requirements or silently drop allocated ones. Any allocation or scope change needs the proper owner and an updated authoritative record.

Every slice, test, and gate must link to at least one justified obligation. IDs have unique definitions; references and parent/sub-requirement links must resolve. Many-to-many links and repeated references are valid. Duplicate definitions, missing allocated IDs, unapproved extras, dangling links, orphaned work, or uncovered obligations are not `PASS`.

For shared requirements, identify this PRD's contribution, other known contributing PRDs, the integration dependency, and the final integrated acceptance owner. Record contribution evidence without calling the whole-system requirement accepted. The architecture owner checks coverage across the committed architecture scope.

Include positive and negative coverage where applicable. Give a reason when a non-behavioral obligation has no meaningful negative case; this cannot exempt an independent semantic guard. Distinguish planned evidence destinations from evidence actually obtained.

### 12. Risks, security, operations, and documentation

- Name concrete correctness, security/privacy, supply-chain, data-loss, compatibility, performance, operational, and rollout risks. Give each relevant risk a trigger, prevention, detection, response, owner, and evidence gate.
- Specify required logs/metrics/traces/audit records, with redaction and retention rules.
- Specify operator/user docs, examples, migration notes, troubleshooting, and release notes, with owners and locations.
- For new permanent support mechanisms, name the dependency or risk addressed, the work or exposure removed, the owner, and a review/removal trigger. Do not add process machinery without a concrete benefit.

### 13. Implementability matrix

End the main PRD with this matrix and the verdict below. Keep the existing row labels. Record PRD-authoring and review context fit under the context-fit row; lineage and integration duties under scope, slices, and coverage; bounded review and recheck evidence under the relevant artifact/handoff rows. Use only `PASS`, `PARTIAL`, or `BLOCKED` for matrix rows, with section/evidence and remaining gap/owner. For a genuinely inapplicable dimension, use `PASS` with an explicit `None —` rationale; this records scoped non-applicability, not a passed runtime test.

| Dimension | Status | Evidence/section | Remaining gap and owner |
| --- | --- | --- | --- |
| Repository or new-project evidence, baseline, and current-state discovery | | | |
| Architecture binding, allocated scope, delegated design, and approval gates | | | |
| Target maturity, operating limits, and permitted claims | | | |
| Source precedence, design authority, and decision closure | | | |
| Outcome, scope, non-goals, and ownership | | | |
| Target worker, context fit, and bounded local choices | | | |
| Interfaces and field-level data contracts | | | |
| Canonical producer/recomputation/verifier closure | | | |
| Cross-artifact admission and consistency where required | | | |
| Non-circular bootstrap, staging, and migration | | | |
| State/effect/transaction/recovery semantics | | | |
| Source/build/install/runtime/platform closure | | | |
| Observed capabilities and filesystem boundaries | | | |
| Integration invalidation and requalification | | | |
| Author-set acceptance rules and schema-valid adversarial cases | | | |
| Supplied artifacts, reference availability, and author-time validation | | | |
| Leaf slices, file ownership, sequencing, and dispatch gates | | | |
| Worker-facing handoffs and fresh-context recipient review | | | |
| Set-equal allocated/local obligation coverage and cross-PRD acceptance ownership | | | |
| Open facts, decisions, assumptions, and late-bound values | | | |
| Security, operations, rollout, and documentation | | | |

Overall classification is non-averaging:

- `PASS` only when every row is `PASS`; all material design decisions are resolved within authority; required author-supplied artifacts and author-time checks/reviews are complete; all slices have defined owners, contracts, and gates; and no unresolved assumption could change the design. Required review coverage includes local obligations, material boundaries, assigned integrated outcomes, every slice's fresh-recipient evidence, and affected rechecks against compatible current bindings. Planned predecessor outputs are permitted only with complete contracts, production steps, acceptance criteria, and a non-circular path to availability.
- `PARTIAL` when the design is useful but authoring, context/handoff repair, artifact validation, or required review/recheck remains incomplete, and no row is `BLOCKED`. Missing review evidence is not a fabricated pass.
- `BLOCKED` when any row is `BLOCKED`: a material authoritative input is unavailable; a decision exceeds authority and lacks resolution; an unresolved fact can change the design; a required dependency has no viable source/producer; or bootstrap/verification is circular. Naming an owner or future investigation does not close the blocker.

Map observations to the claim they affect. An `INCONCLUSIVE` or `NOT_RUN` check cannot satisfy a required proof. If it leaves a design-critical fact unknown, the relevant row is `BLOCKED`; if only a required author-time validation/review remains to run, it is at least `PARTIAL`. A specified future test of not-yet-written code does not lower design readiness merely because it is `NOT_RUN`. At dispatch, any missing required entry proof means `NOT_READY`; at acceptance, missing required evidence prevents acceptance. A known failure must be resolved or handled through an authorized scope/requirement change, never relabeled as success.

Conclude with `Implementation-ready: yes` or `Implementation-ready: no` for this allocated scope, decisive reasons, approval state, inherited approval gates, and a separate dispatch summary. Design `PASS` does not confer approval or grant implementation authority. State which claims have not been established, including implementation acceptance or target-worker performance.

## Mandatory self-review before responding

Audit the complete allocated scope through bounded tasks, using existing coverage notes: question, obligations, exact sources/revisions, dependencies, checks, result/evidence, and unreviewed work. Reconcile the allocation against actual interfaces, shared resources, and lifecycle paths so omissions cannot escape review.

Use local checks of each contribution, artifacts, acceptance, assumptions, and worker handoff; boundary checks of one canonical rule and both sides together; and integrated checks of consumer scenarios and spanning invariants within this PRD's contribution, including combined budgets and lifecycle failures. For divided scenarios, check common assumptions, intermediate results, and joined conclusions.

These are duties, not three agents. Apply the context policy to each task. Give helpers bounded assignments and all applicable governing rules, not the full lead prompt/history by default. The lead reconciles evidence and compatible subject/contract/assumption bindings without repeating every local check. Return cross-scope findings with evidence and owners for bounded investigation; do not ignore them or expand indefinitely.

Track actual obligations and relationships examined, conclusions, evidence, limits, and remaining work. File-open counts, matching IDs, or samples do not establish coverage. Keep review subjects stable; repair canonical material separately and recheck the full affected local, boundary, integrated, and recipient set while retaining valid unrelated evidence. Unrun required checks remain unsatisfied, not closed findings.

Resolve defects and answer all twelve questions across the covered scope:

1. Have you separated current facts, governing requirements, authorized decisions, inferences, and unknowns? Have you resolved all material design choices within your authority?
2. Can the target worker carry out each slice when its entry gate passes without inventing behavior, contracts, acceptance rules, ownership, or undeclared prerequisites?
3. Are all required references real supplied/existing material or explicitly assigned outputs? Are author-supplied contracts and fixture contents present and validated within the claimed scope?
4. Does each relevant datum, artifact, state, and effect have an owner, producer, consumer or retention reason, check, invalidation rule, and recovery behavior where applicable?
5. Are bootstrap and verification non-circular, with a fully specified first step, a viable path to its entry prerequisites, and no proof depending on itself?
6. Do examples obey their contracts? Do semantic negative cases reach their intended guards and assert the right rejection and prohibited effects?
7. Do source, build, install, runtime, platform, integration, rollback, and requalification paths close for the stated scope? Does evidence bind to the right candidate and environment?
8. Do traceability and statuses follow their exact rules? Have you kept design readiness separate from dispatch and implementation acceptance?
9. Do the PRD-authoring scope, review tasks, and each worker packet fit their stated access and full-context needs, preserve one authoritative source, allow harmless local choices, and name a usable exception route? Does each subdivision preserve all parent duties and assign new integration work?
10. Does each control protect a named outcome or risk without weakening mandatory project rules or adding an unnecessary system?
11. Does the PRD preserve the correct architecture and contract revisions, territory links, inherited authority, allocated obligations, shared acceptance owners, and change route without requiring unrelated system requirements in its local coverage check? Do local, boundary, and integrated conclusions agree on their shared assumptions and reviewed bindings?
12. Does a new-project bootstrap or scoped experiment have honest starting-state evidence, complete operating limits, available entry evaluation, and no invented approval, existing code, or production claim?

A failed answer requires correction or a lower status. Self-review alone is not fresh-context or empirical worker evidence.

## Mandatory recipient-consumption review

Before claiming PRD implementation readiness, obtain fresh-context recipient-consumption evidence for **every slice**, using only its worker packet and declared access. One agent, session, or human may cover several slices when context fits; batching or a successful sample cannot cover unreviewed slices. Packet-only access includes declared repository navigation and exact-reference retrieval, not author-only coaching.

Before broad intake, decide who performs the check and preserve that recipient's exposure boundary. The lead may verify existing evidence, but must not expose a planned fresh recipient to prior answers or author-only solutions first. An adversarial reviewer may also serve as recipient only by doing the packet-only pass before broader author-only review. Track exposure per slice: prior repair work or author-only intake can remove freshness for a later dependent check. A context reset, compaction, or role change does not erase exposure.

Ask the recipient, for each slice, to:

1. State the outcome, allocated contribution, baseline, maturity, and operating limits.
2. Name its first substantive actions and locate required inputs, contracts, fixtures, commands, and expected results.
3. Distinguish existing/supplied inputs, accepted-predecessor conditions, current-slice outputs, and permitted late-bound values.
4. Explain normal, error, state/effect, rejection, and recovery behavior, including precedence and prohibited effects where relevant.
5. Identify checks, acceptance rules, evidence, exit gates, downstream consumers, and local versus integrated acceptance owners.
6. State permitted local choices, changes needing authority, and the escalation route.
7. Follow the reading route; report actual retrievals, context/access needs, missing prerequisites, contradictions, guesses, or a design/test standard still to invent.
8. State conditional dispatch status, reasons, and changes that would invalidate the packet or evidence.

A later slice can receive a complete conditional review without pretending its predecessor exists or declaring it executable. Check relevant cross-slice and cross-territory duties, not unrelated internals. Document consumption does not require implementation.

Compare answers with the authoritative packet. Record reviewer, instructions, actual context/access and retrievals, prior exposure, packet/baseline, per-slice coverage, substantive answers, defects, interventions, and disposition. A title, signature, completion message, or “looks complete” is insufficient. Preserve valid unchanged evidence with its binding and reason. Repair canonical material and recheck affected local, counterpart, integrated, and recipient obligations. A recipient who authors a substantive repair cannot supply fresh evidence for that repair; obtain a fresh affected check. Editorial changes that cannot affect consumption need not reopen every slice.

When neither valid current evidence nor a fresh recipient is available, do an accurately labeled author-only check and leave the required review row `PARTIAL`; no overall `PASS`. Stronger self-review, deterministic checks, or the existence of an adversarial report cannot replace the gate. A separate design-changing uncertainty about worker suitability follows the matrix's `BLOCKED` rule, not the routine missing-review rule.

### Bounded target-worker trial

Require a trial when the assignment's review policy calls for it or worker suitability is a material unresolved assumption. Otherwise record whether it ran and limit claims accordingly; a larger reviewer understanding a packet does not prove smaller-worker success.

A trial needs explicit implementation/effect permission, fixed acceptance semantics, and a complete bounded experimental design. Use a representative slice with an actually satisfied dispatch gate under the applicable approvals. If the parent PRD is incomplete, only a separately authorized, independently complete trial scope with its own allocation, permissions, entry conditions, evaluation, containment, and cleanup may run. Do not relabel the incomplete parent or claim its gate passed. The suitability claim being tested is the experiment's output, not its own entry prerequisite; all other applicable design, recipient-review, safety, and execution gates remain binding. Do not create a recursive requirement for a trial to qualify itself.

Fix the exact baseline, packet, worker profile, tools, allowed effects, expected results, and permitted interventions before the run. Record execution, results, missing prerequisites, questions, interventions, rework, and candidate binding. Author rescue or weakened expectations is not unaided success. An unrun trial is `NOT_RUN`; map that missing evidence to the policy and claim it affects. Trial success supports only the tested scope and does not approve or qualify the parent PRD.

## Continuation and working-subject identity

For long work, keep one short operational record in existing work/review notes: current PRD, architecture, and contract revisions; completed and unreviewed scope; findings and evidence locations; affected dependencies; unverified changes; pending decisions; and the next bounded action. Keep review exposure limits where fresh-recipient evidence depends on them. Resume from actual canonical material and recheck changed inputs; a checkpoint is not review evidence, approval, or permission. Preserve operational facts, not a transcript or private reasoning.

Use existing revisions or stable snapshots and a concise change record during content work. Finish substantive edits before optional final metadata. Check delivered contents, safe extraction when an archive is requested, and references from the delivery root. Produce a detached final checksum only when requested, required by governing policy, or justified by a named integrity need. Do not create recurring section hashes, self-hashing or recursive manifests, or metadata repair cycles. A change to meaning, a required location, or a proof-relevant binding triggers affected rechecks; a proven administrative change does not invalidate unrelated semantic evidence. This document policy does not weaken required product integrity checks or pre-execution verification of supplied tools. Save useful partial work and unfinished checks before an actual session limit; do not invent a design blocker or reduce scope silently.

## Delivery rules

Deliver the complete linked PRD and required supporting contents, not an outline, a summary that omits required detail, or a list of files to write later. Use existing project formats, one main entry point, and slice-specific reading routes; do not add an artifact solely because a role exists. Put review evidence and continuation in earlier sections or supporting files so the main PRD still ends with section 13 and its verdict. Include an inventory of supplied files, authoritative references, planned predecessor/current-slice outputs, validation/review results, and any unresolved gaps. This may be a section or table in the PRD rather than a separate manifest.

Return a concise authoring result to the architecture/integration owner: PRD ID and baseline bindings, territory and parent-contribution links, upstream allocations and contribution coverage, justified local requirements, decisions made within delegation, shared-contract or architecture findings and their dispositions, acceptance ownership, readiness/approval/dispatch status, reading entry points, actual artifacts, completed and unreviewed coverage, and evidence. Preserve canonical IDs and revisions so cross-PRD integration does not require rediscovery. This record may be part of section 1 or the inventory; do not invent another mandatory artifact.

Before delivery, check paths/links, unique ID declarations, reference resolution, contract/example agreement, dependency order, review coverage, and status consistency. Report what you checked and what you could not check. Never label `PARTIAL` or `BLOCKED` output implementation-ready, claim a missing artifact exists, or report a test or worker trial that did not run.

Act as an independent, read-only process reviewer for this ongoing project.

Purpose:
Review project progress for friction, churn, unnecessary ceremony, missed efficiencies, weak recovery behavior, and opportunities to improve the reusable operating method. This is primarily a process and execution-system review, not a new product-validation attempt.

Authority and boundaries:
- Remain read-only.
- Do not implement repairs, mutate files, change Beads, create commits, install anything, rerun broad gates, or change external state.
- Do not create new Wayfinder, Reviewer, Validator, handoff, candidate, or planning cycles.
- Use existing thread history, durable checkpoints, evidence, diagnostics, results, and source inspection.
- Do not treat silence, elapsed time, polling timeouts, or agent restarts as evidence of failure.
- Do not reinterpret a deterministic failure as a pass.
- Separate direct observations, source reports, inferences, and recommendations.
- If evidence is incomplete, label the conclusion accordingly rather than commissioning more work.

Review questions:

1. What actor-visible or product progress was actually achieved?
2. Where did execution spend time without advancing the product or milestone?
3. Which failures were genuine product defects, and which were method, environment, subject-binding, fixture, carrier, evidence, authority, ownership, host, or orchestration defects?
4. Were method/setup failures incorrectly treated as candidate failures or semantic successors?
5. Were candidates frozen too early, causing avoidable successor churn?
6. Were deterministic receipts reused when their fingerprints remained current?
7. Were broad gates, reviews, validations, planning cycles, or context compilation repeated without a declared invalidation key?
8. Were Reviewers used for genuine qualitative ambiguity, or merely to record deterministic failures?
9. Were deterministic registered tools used, or did agents hand-roll wrappers, scripts, environment construction, hashing, process capture, or VCS operations?
10. Were subject views correctly distinguished—source root, sealed package, release mirror, installed projection, fixture, and live evidence?
11. Were dependency closure, environment variables, short-path requirements, recorder roots, repository context, and child-process inheritance qualified before expensive or external actions?
12. Did authority or ownership rules prevent unsafe effects, or did they unnecessarily block an already-authorized same-scope continuation?
13. Did Beads provide useful coordination, or did projection mechanics block semantic work without adding safety?
14. Were recovery checkpoints sufficient to resume after interruption without rediscovery or duplicated work?
15. Did status reporting, agent topology, or coordination messages add material value relative to their cost?
16. What worked especially well and should be preserved?

Classify each material friction event using one primary class:

- PRODUCT_DEFECT
- TEST_OR_FIXTURE_DEFECT
- SUBJECT_BINDING_OR_CLOSURE
- METHOD_OR_ENVIRONMENT
- DETERMINISTIC_TOOL_CAPABILITY
- CARRIER_OR_EVIDENCE
- AUTHORITY_OR_OWNERSHIP
- ORCHESTRATION_OR_PROCESS
- HOST_OR_PROVIDER
- EXTERNAL_SYSTEM
- FALSE_ALARM_OR_EXPECTED_BEHAVIOR

For every significant event, record:

- Stable event label or recurrence key
- Exact milestone, WorkUnit, candidate, and operation
- First failing boundary
- Direct evidence and durable references
- Expected versus observed behavior
- Whether product bytes changed
- Whether an external or irreversible effect began
- Whether the event consumed a semantic attempt, only a physical attempt, or neither
- Whether the response was proportionate
- Repeated occurrences or related predecessors
- Workaround or correction used
- Evidence invalidated and evidence safely reused
- Preventability and the earliest point it could have been detected
- Recommended reusable improvement, if any

Pay particular attention to these churn patterns:

- Replanning after scope-preserving mechanical failures
- Reviewer dispatch merely to record or classify deterministic errors
- New candidate revisions caused only by tooling or harness repairs
- Repeated broad validation against unchanged inputs
- Repeated authority requests despite a current standing grant
- Wrong package/source/install subject comparisons
- Ad hoc PowerShell, Python, hashing, process-capture, or VCS wrappers
- Missing dependency or environment closure discovered only during expensive gates
- Long-path, repository-context, hidden-file, or child-environment surprises
- Tracker or Beads workflow state being confused with canonical BBK lifecycle state
- Excessive checkpoint, handoff, schema, or agent ceremony without a corresponding risk
- Parent agents doing work that belonged to a deterministic tool or bounded Worker
- Failure to batch related corrections before freezing the next candidate

Quantify only when the evidence supports it. Useful metrics include:

- Product defects versus method/process defects
- Semantic candidates versus physical attempts
- Broad-gate executions and avoidable repeats
- Planning, Reviewer, and Validator invocations
- Failures occurring before meaningful execution or external effect
- False semantic successors
- Reused versus unnecessarily regenerated evidence
- Interruptions recovered without rediscovery
- Time or iteration count from first failure to root-cause localization

Required output:

1. Executive assessment
   - Current progress and readiness
   - Overall friction level: LOW, MODERATE, HIGH, or CRITICAL
   - Whether the project should CONTINUE_AS_IS, CONTINUE_WITH_LOCAL_CORRECTIONS, SIMPLIFY_ROUTE, PAUSE_FOR_METHOD_REPAIR, or REPLAN

2. Progress timeline
   - Concise milestone/attempt sequence
   - Distinguish product progress from process activity

3. Friction ledger
   - A compact table of material events using the fields above
   - Group repeated symptoms under one recurrence lineage

4. Root causes
   - Separate immediate causes from systemic causes
   - Identify which issues belong to the product, tests, deterministic tooling, BBK method, host, or project-specific execution

5. Efficiencies and strengths
   - Evidence reuse, deterministic tooling, containment, recovery, batching, narrow repairs, or other practices that worked well

6. Waste and avoidable churn
   - Name the specific work that could have been avoided
   - Explain the earliest safe intervention that would have prevented it

7. Recommendations
   For each recommendation provide:
   - Priority: P0, P1, P2, or P3
   - Scope: CURRENT_CAMPAIGN, REUSABLE_TOOLING, BBK_METHOD, PROMPT_OR_DOCUMENTATION, or LEARNING_CANDIDATE
   - Exact proposed change
   - Evidence supporting it
   - Expected benefit
   - Risk or tradeoff
   - Responsible semantic owner
   - Trigger for applying it
   - Whether it should happen now or after the current milestone

8. What not to change
   - Safeguards or procedures that looked expensive but demonstrably prevented a real risk
   - Recommendations that would weaken authority, candidate immutability, independent assurance, evidence preservation, or external-effect safety

9. Immediate continuation guidance
   - The smallest one to three next actions
   - Evidence that can be reused
   - Work that must not be repeated
   - Exact conditions that would justify escalation

10. Learning candidates
   - A short list of recurring, evidence-supported improvements for later BBK/tooling refinement
   - Do not automatically change the method or treat a learning candidate as accepted policy

Be direct and critical. Prefer concrete evidence over general process advice. Challenge unnecessary ceremony as strongly as unsafe shortcuts. The goal is to improve throughput and reliability without weakening authority boundaries, deterministic evidence, candidate integrity, recovery safety, or truthful completion claims.
```

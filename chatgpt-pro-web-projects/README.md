# Blueprint / BBK One-Shot Implementation Kit v2.0

Contents:

- `blueprint-bbk-one-shot-implementation-prompt-v2-compact.md` — recommended default prompt.
- `blueprint-bbk-one-shot-implementation-prompt-v2.md` — expanded high-assurance variant.
- `one-shot-blueprint-bbk-toolkit-guide.md` — prioritized tools and offline packaging guidance.
- `one-shot-tool-bundle-manifest.example.yaml` — example manifest for supplied binaries, toolchains, and caches.
- `SHA256SUMS` — content digests for this package.

Revision 2.0 changes the execution model from “do not initialize Git/Beads/jj” to a proportional disposable-substrate policy:

- ephemeral Git is the normal choice for nontrivial unversioned file work;
- existing Git or Jujutsu repositories are preserved and used according to their conventions;
- Beads is conditional on a meaningful work graph and kept outside the deliverable;
- supplied tools are pinned, verified, task-local, and do not grant effect authority;
- genuine sub-agents are detected rather than assumed;
- when sub-agents are unavailable, the agent uses separated review passes and stronger deterministic evidence without claiming independence.

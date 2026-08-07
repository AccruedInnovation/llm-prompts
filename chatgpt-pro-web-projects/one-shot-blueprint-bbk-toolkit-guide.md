# Tool Kit for One-Shot Blueprint / BBK Implementation Work

**Snapshot date:** 2026-07-25  
**Target environment observed in this session:** Debian 13 (`trixie`), Linux `x86_64`, glibc 2.41

This guide describes tools that are useful to attach to a one-shot implementation request when the execution shell may have no outbound package-registry or GitHub access. The tool bundle is an implementation aid, not an authority grant: its contents do not authorize network access, credentials, publication, deployment, remote mutation, or destructive actions.

## 1. What is already available in the current environment

The current container already includes a strong base:

- Git, `patch`, `diff`, `sha256sum`, `tar`, `zip`, `unzip`, and `rsync`;
- `ripgrep`, `jq`, `sed`, `awk`, Perl, and standard GNU utilities;
- Python 3.13, `uv`, `pip`, and `pytest`;
- Node.js 22, npm, and `npx`;
- Go 1.23;
- GCC, G++, Clang, Make, CMake, Ninja, Autoconf, and Automake;
- Pandoc;
- Playwright and Chromium.

It currently does **not** include Beads, Jujutsu, Rust/Cargo, `yq`, `ast-grep`, Difftastic, ShellCheck, `shfmt`, Gitleaks, Syft, Grype, Hyperfine, Typos, Lychee, the SQLite CLI, or the DuckDB CLI.

The exact image may change between sessions. The implementation prompt therefore requires the agent to re-inventory the environment instead of assuming this snapshot remains true.

## 2. Highest-value tools to supply

### 2.1 Beads (`bd`) — conditional default for work graphs

**Supply when:** the task has several dependent units, multiple implementation workstreams, significant discovered work, several blockers/findings, or repeated repair and validation loops.

**Do not supply merely because:** the task is a coherent one- or two-file change.

**Recommended package:** the stable Linux AMD64 release archive, its official checksum file, and a short note identifying the version. Beads v1.1.0 is the current stable release at this snapshot date.

**One-shot use:** task-local state, explicit `BEADS_DIR`, stealth/non-invasive initialization, and one authoritative writer in embedded mode. The lead agent should write the graph; sub-agents, when genuinely available, should return structured updates for the lead to record. Server mode is justified only for actual concurrent writers and requires additional lifecycle and cleanup machinery.

**Why it helps:** dependency-aware ready work, stable identities, discovered-work capture, blocker tracking, and repair-loop closure.

### 2.2 Jujutsu (`jj`) — useful, but not a default requirement

**Supply when:** the subject already uses `jj`, the task benefits from several isolated workspaces or change lines, or operation-log recovery and change-oriented history materially improve the work.

**Usually omit when:** ordinary ephemeral Git already provides enough baseline capture, diffing, rollback, and final-candidate identity.

**Recommended package:** a pinned Linux x86_64 release binary and checksum. Jujutsu v0.43.0 is the current release at this snapshot date.

**Important:** when a repository is colocated with Git, the agent must inspect and respect that mode. It should not casually alternate mutating Git and `jj` commands.

### 2.3 `yq` — high-value structured-data utility

A portable `yq` binary is one of the best small additions. It provides reliable YAML editing and querying and also handles several adjacent structured formats. This is particularly valuable for CI files, manifests, configuration, Kubernetes-like YAML, and generated metadata.

Supply a pinned standalone binary and checksum. Avoid relying on similarly named Python packages because their CLI and semantics differ.

### 2.4 `ast-grep` — syntax-aware search and transformation

Supply `ast-grep` for large or cross-cutting code changes where text search and regex replacement are too fragile. It performs syntax-aware structural search, linting, and rewriting across many languages.

Use the executable name `ast-grep`, not `sg`. In the current Debian image, `/usr/bin/sg` is an unrelated Unix account/group command, and current ast-grep releases are deprecating the `sg` alias.

This tool is especially useful for:

- repository-wide API migrations;
- locating syntactic patterns rather than text fragments;
- proving that prohibited patterns are absent;
- making mechanical rewrites while preserving surrounding code.

### 2.5 Difftastic (`difft`) — better human and agent review of code changes

Difftastic compares code structurally rather than only line by line. It is useful for reviewing refactors, reformats, and generated changes where an ordinary diff obscures the semantic edit.

It should supplement, not replace, ordinary Git diffs and exact candidate manifests. A statically linked or musl Linux binary is preferable when available.

### 2.6 Gitleaks — secret and credential scanning

Supply Gitleaks for repositories, configuration bundles, deployment artifacts, or generated packages that might contain credentials, tokens, private keys, or copied secrets.

Treat findings as findings, not automatic proof of a real secret. Test fixtures and high-entropy identifiers can produce false positives and require explicit disposition.

### 2.7 Syft, and optionally Grype — package inventory and dependency risk

**Syft** is useful whenever the deliverable is a release archive, binary distribution, container filesystem, or dependency-heavy package. It can create an SBOM from filesystems and artifacts without requiring a live service.

**Grype** scans filesystems or SBOMs for known vulnerabilities. For an offline execution shell, the binary alone is insufficient for a useful current scan: provide a compatible vulnerability database snapshot and record its date and digest. A stale database must be reported as stale rather than treated as current evidence.

For many one-shot jobs, Syft is useful while Grype is optional.

### 2.8 Hyperfine — reproducible command benchmarking

Supply Hyperfine when performance, build speed, startup time, serialization, migration, or query latency is part of the acceptance criteria. It produces repeated measurements and machine-readable results and is far better than one-off `time` output.

Benchmarks still require warm-up, controlled inputs, environment disclosure, and correctness checks. A faster incorrect command is not a successful result.

## 3. Small, situationally valuable tools

### Shell and CI work

- **ShellCheck** — static analysis for shell scripts.
- **`shfmt`** — deterministic shell formatting.
- **Hadolint** — Dockerfile linting, when Dockerfiles are part of the subject.
- **actionlint** — GitHub Actions workflow validation.

Supply these when the matching file type is present; they need not be in every bundle.

### Documentation and package hygiene

- **Typos** — low-noise source-code typo checking.
- **Lychee** — local and external link checking for Markdown, HTML, and related formats. External-link checks require network; local-link checks do not.
- **Vale** — prose/style linting when the project already has a Vale configuration.

Do not introduce a new prose style regime merely because a linter is available.

### Data and substrate work

- **SQLite CLI** — direct inspection, `.dump`, integrity checks, and controlled fixtures.
- **DuckDB CLI** — useful for Parquet/CSV/Arrow analysis and analytical verification.
- **Standalone Dolt CLI** — supply only when the task genuinely requires Beads server mode, direct Dolt inspection, or Dolt-specific fixtures. Ordinary Beads embedded use does not justify it by itself.

### Debugging and failure analysis

These are valuable for native binaries, sidecars, subprocess orchestration, file locks, and crash/recovery work:

- `strace`;
- `lsof`;
- GDB;
- Valgrind;
- `perf`, where the container permits performance counters;
- `socat` and netcat, already present in the current image, for protocol fixtures.

These tools are usually distributed as Debian packages with library dependencies rather than clean standalone binaries. Supply a complete offline `.deb` set for Debian 13/x86_64 or a tested self-contained package, not a lone executable copied from an arbitrary system.

### Command runners

- **`just`** is a simple project-command runner.
- **Task** is a cross-platform task runner with YAML Taskfiles and caching features.

Supply one only when the project already uses it or the requested deliverable explicitly includes a reproducible command surface. Do not add both, and do not replace an existing Makefile, npm script, Cargo command, or project-native runner merely for preference.

## 4. Task-specific toolchains matter more than a giant universal bundle

The most valuable attachment is often the exact language toolchain and offline dependency closure needed by the project.

### Rust

The current environment has no Rust toolchain. For Rust work, supply a complete tested toolchain bundle rather than only `rustup-init`, which normally downloads components.

At minimum include:

- `rustc` and Cargo;
- standard library for the target;
- `rustfmt` and Clippy;
- target linker/runtime requirements;
- the project's vendored dependencies or a complete Cargo registry/git cache;
- the exact `rust-toolchain.toml` or version declaration.

Useful optional tools include `cargo-nextest`, coverage tooling, `cargo-deny`, `cargo-audit` with an offline advisory database, and the mutation-testing tool selected by the project profile.

### Python

The environment already has Python, `uv`, and `pytest`, but project dependencies may be unavailable offline. Supply:

- a lockfile;
- a wheelhouse containing every direct and transitive dependency for Linux x86_64/Python 3.13, or a project-supported Python version plus its complete environment;
- Ruff, Pyright or mypy, Hypothesis, coverage, and other tools required by the project profile.

### TypeScript / JavaScript

Node and npm are present, but the registry may be unreachable. Supply one of:

- a complete lockfile-matched npm cache;
- a project `node_modules` archive produced for compatible Linux x86_64/Node ABI;
- a vendored package store for the project's selected package manager.

Include the project's actual TypeScript, lint, test, bundler, and browser-test dependencies. For web UI work, the current image has Playwright and Chromium, but a future session may require a supplied browser bundle.

### Go

Go is present, but modules may not be cached. Supply a `vendor/` tree or a complete lock-consistent module cache. Optional verification tools include Staticcheck, `govulncheck` with appropriate data availability, `golangci-lint`, `gofumpt`, and `gotestsum`.

### C and C++

The base compilers and build tools are present. Supply project-specific SDKs, headers, libraries, code generators, cross-compilers, and exact sanitizer/debug dependencies. `clang-tidy`, `clang-format`, and `cppcheck` are useful additions when the project expects them.

### Protocol and schema work

Supply the exact generator and runtime closure selected by the project, such as:

- `protoc` and required plugins;
- Buf;
- FlatBuffers compiler;
- Cap'n Proto compiler;
- OpenAPI generators;
- JSON Schema validators;
- database migration CLIs.

Generated bindings are candidate-bound evidence only when the exact generator version, input schemas, flags, and output digests are recorded.

## 5. Real sub-agents require more than a binary

Beads is a work graph, not an agent runtime.

To enable genuine sub-agents in a one-shot container, the supplied system would need to expose a real task-agent or model-invocation primitive. A project-specific harness such as OMP could potentially provide that, but a binary alone is insufficient. The request must also provide or authorize:

- a runnable harness and its complete dependencies;
- model/provider configuration;
- credentials or a local model endpoint;
- network access where required;
- model-spend and concurrency authority;
- workspace/isolation behavior;
- structured result and cancellation semantics.

Without those conditions, the lead model can still use Git, Beads, local subprocess concurrency, deterministic checks, and separated review passes, but it must not claim that real sub-agents were used.

## 6. Recommended bundle shapes

### Minimal coordination bundle

Use for a medium or large implementation task:

```text
tooling/
  manifest.yaml
  SHA256SUMS
  bin/
    bd
    yq
    ast-grep
    difft
  licences/
  README.md
```

Add `jj` only when justified.

### Assurance bundle

Add when release, security, dependency, documentation, or performance evidence matters:

```text
tooling/
  bin/
    gitleaks
    syft
    grype
    hyperfine
    shellcheck
    shfmt
    typos
    lychee
  data/
    grype-db/
  licences/
```

### Language bundle

Keep language toolchains and dependency caches separate so they can be attached only to matching tasks:

```text
rust-toolchain/
python-wheelhouse/
node-offline-store/
go-vendor-or-modcache/
protocol-codegen/
```

## 7. Packaging rules

For this environment, prefer Linux `x86_64` binaries that are either statically linked or known to run on Debian 13/glibc 2.41. Include:

- exact version;
- upstream project and release identity;
- SHA-256 digest;
- licence file;
- executable path;
- whether the binary is static or its runtime-library requirements;
- whether it requires network or an external database;
- any bundled data snapshot date and digest;
- a brief purpose and invocation note.

A release archive plus its official checksum is better than an installation script that downloads unknown current content. Avoid supplying:

- unpinned `curl | sh` installers;
- binaries without provenance or licence information;
- only `rustup-init`, npm, pip, or another bootstrap client when the shell may be offline;
- container images without a working Docker/Podman runtime;
- both `just` and Task without a project reason;
- standalone Dolt for ordinary single-writer Beads use;
- huge security databases with no snapshot date;
- tools that duplicate project-native checks but produce no additional assurance.

## 8. Recommended default request wording

Paste this into the assignment when tools are attached:

```text
## Supplied Tools and Execution Substrate

The attached `tooling/` directory contains pinned task-local tools. Verify
`SHA256SUMS` before execution, use only the binaries relevant to this task,
record their effective versions and digests, and do not install them globally.
The presence of a tool does not authorize network access, credentials,
publication, deployment, remote mutation, or destructive effects.

Use ephemeral Git for nontrivial unversioned file work. Use Beads only when the
work has a meaningful dependency graph or repair/findings lifecycle. Keep
Beads state outside the deliverable and use one authoritative writer unless a
concurrent mode is explicitly authorized and verified. Use `jj` only when it
adds material value or is already part of the project.

No genuine sub-agent capability should be assumed unless the execution host
actually exposes a separately invokable task-agent/model facility.
```

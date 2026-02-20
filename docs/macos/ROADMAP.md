# macOS Apple Silicon Roadmap

## Objective

Deliver a single-repo RetroBat distribution that works on:
- Windows (existing support, unchanged behavior)
- macOS (Apple Silicon only)

## Non-Goals

- macOS Intel support
- Upstream pull requests before full fork-level validation

## Phases

## Phase 0 — Foundation

Deliverables:
- Branching and governance model active
- PR/issue templates active
- Local push guardrails active
- Test gate workflow active

Exit criteria:
- Team can open and review platform-scoped PRs with policy checks
- Accidental upstream push attempts are blocked locally

## Phase 1 — Platform Abstraction

Deliverables:
- OS-aware launcher/config abstraction
- Path handling normalization (Windows/macOS)
- Shell execution abstraction (PowerShell/CMD vs zsh/bash)

Exit criteria:
- Core bootstrap flow runs on both platforms without changing Windows behavior

## Phase 2 — macOS Runtime Baseline (Apple Silicon)

Deliverables:
- Baseline emulator matrix for macOS supported set
- First-run setup and dependency checks for macOS
- Logging parity for diagnostics

Exit criteria:
- Smoke scenario (install → scan → launch) passes on Apple Silicon

## Phase 3 — Compatibility Expansion

Deliverables:
- Incremental emulator/system support expansion
- Config migration and compatibility improvements
- User-facing docs for macOS flows

Exit criteria:
- Feature parity target list completed for selected systems

## Phase 4 — Stabilization and Release Candidate

Deliverables:
- Regression and stress validation
- Known-issues triage burn-down
- Release packaging and release notes draft

Exit criteria:
- RC quality gate passes with no blocker defects

## Phase 5 — Fork GA

Deliverables:
- GA release in fork
- Post-release monitoring and patch process

Exit criteria:
- Stable operation over defined soak period

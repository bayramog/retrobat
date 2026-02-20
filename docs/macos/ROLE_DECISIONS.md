# macOS Expansion Role Decisions

This document records decisions made by three roles for the `bayramog/retrobat` fork.

## Roles

- **Program Manager (PMg):** scope governance, release confidence, cross-team alignment.
- **Project Manager (PM):** delivery planning, dependencies, execution cadence.
- **Test Manager (TM):** test gates, release quality, validation strategy.

## Decision Session #1 — Platform Scope

### PMg
- Keep existing Windows behavior intact.
- Add macOS support in the same repository.
- Limit macOS hardware target to **Apple Silicon only** (no Intel support).

### PM
- Deliver in phases with strict exit criteria.
- Avoid broad emulator coverage first; start with a validated baseline set.
- Build a branch strategy that keeps unstable work out of `main`.

### TM
- Require test gates per phase.
- Require explicit smoke validation on macOS Apple Silicon before phase closure.
- Block releases when critical launch/config regressions are open.

## Agreed Decisions

1. The fork remains a **single codebase** supporting Windows + macOS Apple Silicon.
2. Windows behavior is treated as a protected compatibility baseline.
3. No PR from this fork to upstream until:
   - all phase gates are passed,
   - macOS feature parity target (defined in roadmap) is achieved,
   - release candidate quality is accepted.
4. Upstream may be fetched for sync; upstream must never be a push target.

## Decision Session #2 — Governance and Delivery

### PMg
- Use explicit integration branch for macOS stream.
- Force structured PR reviews and quality checks.

### PM
- Use branch naming conventions to distinguish work type and platform impact.
- Use milestones for Alpha, Beta, RC, GA.

### TM
- Define minimum gates for all PRs and stricter gates for release branches.
- Keep manual test checklist mandatory for user-facing flows.

## Agreed Decisions

1. Primary integration flow is `feature/* -> macos/integration -> release/* -> main`.
2. Branch policies are enforced by CI and repository settings.
3. Test and validation policy is mandatory for every merge target.

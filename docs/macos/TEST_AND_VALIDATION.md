# Test and Validation Strategy

## Quality Principles

- Windows behavior remains backward compatible.
- macOS target is Apple Silicon only.
- Promotion between phases requires objective gate results.

## Mandatory Gates

## Gate A — PR Policy Gate

Required for all PRs:
- Branch naming policy
- Base branch policy
- PR checklist completeness

## Gate B — Static Validation

Required for all PRs:
- Script syntax checks (`.sh`, `.command`)
- Configuration consistency checks (required docs/policies present)

## Gate C — Functional Smoke

Required for platform-impacting PRs:
- Startup flow
- ROM discovery/scan flow
- One-launch-per-priority system flow

## Gate D — Regression Pack

Required for release branches:
- Windows regression smoke
- macOS Apple Silicon regression smoke
- Known critical flows from previous releases

## Gate E — Release Readiness

Required for `release/macos-*`:
- Blocker bugs: 0
- High severity bugs: accepted or fixed
- Manual QA checklist complete

## Test Matrix

Supported runtime matrix:
- macOS Apple Silicon (required)
- Windows stable baseline (required)

Not supported:
- macOS Intel

## Definition of Done (DoD)

A task is done only when:
- Code merged under branch policy
- Required gates green
- Documentation updated
- No new critical Windows regression

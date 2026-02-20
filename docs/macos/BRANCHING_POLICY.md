# Branching and Release Policy

## Core Rule

No pull request from this fork is sent to upstream until fork objectives are fully validated.

## Long-Lived Branches

- `main`: stable branch for the fork.
- `macos/integration`: integration stream for macOS work.
- `release/macos-alpha`, `release/macos-beta`, `release/macos-rc`: release stabilization branches.

## Working Branches

- `epic/macos-<scope>`
- `feature/macos-<scope>`
- `fix/macos-<scope>`
- `chore/macos-<scope>`
- `feature/windows-<scope>` / `fix/windows-<scope>` only when required to preserve Windows compatibility.
- `feature/cross-<scope>` / `fix/cross-<scope>` for shared cross-platform abstractions.

## Merge Flow

1. Branch from `macos/integration` for macOS/cross work.
2. Open PR back into `macos/integration`.
3. Promote to `release/macos-*` during stabilization windows.
4. Merge release branch into `main` after all gates pass.

## Required Repository Settings

Apply branch protection to `main`, `macos/integration`, `release/*`:
- Require pull request before merge.
- Require at least 2 approvals.
- Require status checks to pass.
- Block force-push.
- Block direct pushes.

## Upstream Usage

- Allowed: `git fetch upstream`, compare/rebase as needed.
- Forbidden: any push to upstream remote.

# Local Development Workflow

## Local Git Remotes

Expected remotes:
- `origin` -> `bayramog/retrobat` (push target)
- `upstream` -> `RetroBat-Official/retrobat` (fetch-only source)

## One-Time Setup

1. Configure remotes:

```bash
git remote add upstream https://github.com/RetroBat-Official/retrobat.git
git remote -v
```

2. Install local git hooks:

```bash
./tools/dev/install-git-hooks.sh
```

3. Verify pre-push guard:

```bash
git push upstream HEAD
```

Expected: push is blocked by hook.

## Daily Workflow

1. Sync:

```bash
git fetch upstream
git checkout macos/integration
git pull origin macos/integration
```

2. Start branch:

```bash
git checkout -b feature/macos-<scope>
```

3. Commit and push:

```bash
git push -u origin feature/macos-<scope>
```

4. Open PR to `macos/integration`.

## Release Workflow

```bash
git checkout -b release/macos-alpha
git push -u origin release/macos-alpha
```

Repeat for beta/rc. Merge to `main` only after release gates pass.

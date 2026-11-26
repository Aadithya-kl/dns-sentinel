# Contributing

Thanks for helping make DNS Sentinel accurate and useful. Contributions should be small, tested, and clear about their limits.

## Before opening a pull request

1. Search existing issues and explain the use case or standards requirement.
2. For protocol behavior, cite the relevant RFC or authoritative documentation.
3. Add deterministic tests. Unit tests must not depend on public DNS or a real domain.
4. Run `pytest`, `ruff check .`, `mypy`, and `python -m build` locally.
5. Describe behavior changes and any remaining limits in the pull request.

## Scope and review

Avoid broad rewrites and new dependencies without a concrete need. Never add active probing, credential collection, or DNS mutations without prior discussion. A passing CI run does not establish protocol correctness; reviewers will check claims against evidence and standards. Maintainers aim to acknowledge issues within seven days and review pull requests within fourteen days, subject to availability; these are goals, not guarantees.

## First contributions

Look for issues labeled `good first issue` and ask for clarification before spending substantial time. A contribution is considered merged only when accepted into the default branch. The project does not promise acceptance or any external qualification outcome.

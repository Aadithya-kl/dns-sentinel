# Releasing

The package is not published to PyPI yet. The GitHub release workflow uses PyPI Trusted Publishing, so no long-lived PyPI token is stored in GitHub.

## One-time PyPI setup

1. Sign in to the PyPI account that will own `dns-sentinel` (or create that account).
2. In PyPI's Trusted Publishers settings, add a GitHub Actions publisher with:
   - Owner: `kkevadiya54`
   - Repository: `dns-sentinel`
   - Workflow: `publish.yml`
   - Environment: `pypi`
3. Keep the PyPI account's recovery methods current. Do not put an API token in a repository secret for this workflow.

## Release a version

1. Update the project version in `pyproject.toml` and the changelog/release notes.
2. Run unit tests, lint, type checks, integration tests where network access is available, and `python -m build`.
3. Merge the release change through a pull request and wait for CI.
4. Create and publish a GitHub release for the matching version tag (for example `v0.1.0`).
5. Confirm the `Publish to PyPI` workflow succeeded and verify the installed distribution from a clean environment.

PyPI releases are public and cannot be silently replaced. Publish only after reviewing the built artifacts and release notes. The first release remains pending until the account owner completes the PyPI publisher setup.

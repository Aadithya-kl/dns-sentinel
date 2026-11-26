# Community growth plan

The long-term aspiration is 20 unique external contributors with merged pull requests in a rolling 12-month period. It is an outcome, not a promise or a qualification claim. Contributions must come from genuine, independent people; no alternate accounts, paid low-quality PRs, artificial stars, or fabricated usage will be counted.

## Make useful work visible

- Publish a tested release and a short demo showing what the tool can and cannot conclude.
- Share standards-backed findings and reproducible bug reports with DNS, Python, security engineering, and open-source communities. Follow each community's self-promotion rules; do not spam.
- Ask a small number of practitioners to review specific protocol checks, rather than asking broadly for stars.
- Write short notes when a standards nuance changes a finding, with test vectors and links to the relevant RFC.

## Give newcomers a reliable first experience

- Keep a public `good first issue` queue with exact expected behavior, pointers to code, and acceptance tests. Create issues only after confirming they are real and in scope.
- Keep issues small enough to complete in a few hours; examples include a standards test vector, clearer error wording, or one isolated parser edge case.
- Maintain a contributor setup that works from a clean clone and CI that runs the same checks.
- Acknowledge new reports promptly, explain decisions respectfully, and credit accepted contributions in release notes.
- Do not label work `good first issue` if it needs undisclosed design work or maintainer-only access.

## Build trust and retain contributors

- Prefer RFC citations, captured evidence, and regression tests over popularity claims.
- Publish release notes, known limitations, and response expectations. If maintainer capacity changes, update those expectations openly.
- Review external pull requests for correctness and scope; do not merge PRs just to increase a count.
- Track only public, verifiable project signals: unique outside contributors whose PRs actually merged, time to first maintainer response, and repeat contributors. Review the rolling 12-month contributor count quarterly.
- Invite contributors to choose work; do not promise jobs, credentials, or qualification outcomes.

## First 90 days after publishing

1. Confirm install, CLI, tests, and CI from a clean clone; address issues before promotion.
2. Ask several DNS/mail practitioners for technical review and incorporate feedback with tests.
3. Open a small set of real issues from documented limitations: SPF edge cases, DMARC URI handling, CAA properties, and resolver test fixtures.
4. Share one practical tutorial and one short demo in appropriate communities, following their rules.
5. Review engagement monthly. If there are no external contributions, improve utility and onboarding instead of manufacturing activity.

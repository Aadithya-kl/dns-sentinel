# Roadmap

This roadmap describes intent, not promises. Work is prioritized by correctness, reproducibility, and maintainability; timelines depend on contributors and review capacity.

## MVP (0.1.x)

- [x] Read-only CLI and Python API
- [x] Per-query DNS failure handling and machine-readable JSON
- [x] Basic SPF, DMARC, CAA, MX, NS, and DNSSEC record-presence checks
- [x] Deterministic unit tests, packaging, and CI foundations
- [x] PyPI Trusted Publishing release workflow and provenance attestations
- [ ] Independent review against relevant RFCs, including RFC 9989, before stable release

## Next (0.2)

- RFC-driven test vectors and stronger record parsing, especially SPF mechanisms and CAA properties
- Explicit resolver configuration and reproducible integration test harness
- Optional authoritative-delegation consistency checks
- Output schema versioning and stable severity/status definitions

## Later (0.3+)

- Optional, clearly separated cryptographic DNSSEC validation using a vetted validator/library
- Mail DNS checks for DKIM selectors only when explicitly supplied by the user
- Baseline comparison and monitoring integrations, only with transparent privacy controls
- OpenSSF Scorecard review

## Out of scope until reviewed

Full SPF policy evaluation is easy to get wrong and can trigger DNS amplification/lookup-limit issues. Complete DNSSEC validation requires correct trust-anchor and chain handling. These will not be implied by superficial record checks. No target contributor counts, stars, downloads, or qualification results are guaranteed or manufactured.

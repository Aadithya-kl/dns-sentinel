# DNS Sentinel

DNS Sentinel is a read-only command-line tool and Python library for a first-pass review of public DNS security configuration. It checks SPF, DMARC, CAA, MX, nameserver count, and DNSSEC record presence. It is an early MVP: findings are evidence-based hints, not a compliance certificate or a substitute for a mail/DNS specialist.

## Install and run

Requires Python 3.10 or newer.

```sh
python -m pip install dns-sentinel
dns-sentinel example.com
dns-sentinel example.com --json
```

Exit status is 0 when no error-severity findings exist, 1 when an error-severity finding exists, and 2 when input or runtime setup prevents an audit. Warnings can indicate missing controls or incomplete answers. Network timeouts are reported per check and do not discard other results.

Use only for domains you are authorized to assess. The tool sends ordinary DNS queries to the system-configured recursive resolver; it does not scan hosts, change DNS, or send email.

## Check limits

- **SPF:** Detects zero or multiple policies and checks basic token syntax. It does not fully evaluate RFC 7208 policy semantics, includes, redirects, DNS lookup limits, or authorization outcomes.
- **DMARC:** Requires one _dmarc TXT policy and validates version, policy, duplicate tags, pct, and basic rua syntax. It does not implement all RFC 7489/9091 semantics or process reports.
- **CAA:** Checks returned CAA tags and flags. It does not fully implement tree-walk inheritance or issuer authorization semantics.
- **MX:** Checks preference and exchange shape, duplicate targets, and RFC 7505 null MX. It does not verify mail host reachability.
- **NS:** Counts distinct returned nameserver targets. It does not verify operator, network, or geographic independence.
- **DNSSEC:** Reports whether DNSKEY and DS records were observed. This is a record-presence check only; this tool does **not** cryptographically validate signatures or the chain of trust.

Resolver failures are distinguished from negative answers. A timeout, nameserver failure, or local resolver problem is not proof that a record is absent.

## Python API

```python
from dns_sentinel import Auditor

report = Auditor(timeout=2, lifetime=5).audit("example.com")
for finding in report.findings:
    print(finding.check, finding.status, finding.message)
print(report.to_dict())
```

## Development

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install -e '.[dev]'
pytest --cov=dns_sentinel --cov-report=term-missing
ruff check .
mypy
python -m build
```

Unit tests use deterministic resolver fakes; they do not depend on public DNS. The live integration test can be run with `pytest -m integration -o addopts=''`.

Read [CONTRIBUTING.md](CONTRIBUTING.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), [SECURITY.md](SECURITY.md), and [COMMUNITY.md](COMMUNITY.md) before contributing. See [ROADMAP.md](ROADMAP.md) for planned work and known limits.

## Project status

Alpha software. No adoption, external contributors, package downloads, or certifications are claimed. The project aims to grow a genuine contributor community; it does not guarantee a contributor count or qualification result.

## License

MIT; see [LICENSE](LICENSE).

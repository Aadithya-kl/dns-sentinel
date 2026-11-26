"""Command-line interface for DNS Sentinel."""

from __future__ import annotations

import argparse
import json
import sys

from dns_sentinel import Auditor, __version__
from dns_sentinel.auditor import normalize_domain


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only DNS security configuration audit")
    parser.add_argument("domain", help="Domain name, such as example.com")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    parser.add_argument(
        "--timeout", type=float, default=2.0, help="Per-query DNS timeout in seconds"
    )
    parser.add_argument(
        "--lifetime", type=float, default=5.0, help="Maximum lifetime per DNS query in seconds"
    )
    parser.add_argument("--version", action="version", version=f"dns-sentinel {__version__}")
    args = parser.parse_args()
    try:
        domain = normalize_domain(args.domain)
        report = Auditor(timeout=args.timeout, lifetime=args.lifetime).audit(domain)
    except ValueError as exc:
        parser.error(str(exc))
    except Exception as exc:  # Last-resort boundary for an OS/resolver failure.
        print(f"dns-sentinel: audit could not complete: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(report.to_dict(), indent=2))
    else:
        print(f"DNS Sentinel audit: {report.domain}")
        for finding in report.findings:
            print(f"[{finding.status.upper():7}] {finding.check}: {finding.message}")
            for item in finding.evidence:
                print(f"           {item}")
    return 0 if report.passed else 1


if __name__ == "__main__":
    raise SystemExit(main())

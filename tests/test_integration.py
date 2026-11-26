import pytest

from dns_sentinel import Auditor


@pytest.mark.integration
def test_public_dns_end_to_end() -> None:
    report = Auditor(timeout=3, lifetime=8).audit("example.com")
    assert report.domain == "example.com"
    assert {finding.check for finding in report.findings} == {
        "spf",
        "dmarc",
        "caa",
        "mx",
        "ns",
        "dnssec_record_presence",
    }
    assert all(
        finding.status in {"pass", "fail", "error", "unknown"} for finding in report.findings
    )

import pytest

from chrome_fingerprints import FingerprintGenerator


@pytest.fixture
def fingerprint_generator() -> FingerprintGenerator:
    fp_gen = FingerprintGenerator()
    return fp_gen

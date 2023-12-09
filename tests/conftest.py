import pytest
import pytest_asyncio

from chrome_fingerprints import FingerprintGenerator, AsyncFingerprintGenerator


@pytest.fixture
def fingerprint_generator() -> FingerprintGenerator:
    fp_gen = FingerprintGenerator()
    return fp_gen


@pytest_asyncio.fixture
async def async_fingerprint_generator() -> AsyncFingerprintGenerator:
    fp_gen = AsyncFingerprintGenerator()
    return fp_gen

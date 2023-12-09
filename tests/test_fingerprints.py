import time
from chrome_fingerprints import FingerprintGenerator, ChromeFingerprint


def test_fingerprint_random(fingerprint_generator: FingerprintGenerator):
    chrome_fp = fingerprint_generator.get_fingerprint()
    assert isinstance(chrome_fp, ChromeFingerprint)


def test_fingerprint_index(fingerprint_generator: FingerprintGenerator):
    chrome_fp = fingerprint_generator.get_fingerprint(fingerprint_index=0)
    assert isinstance(chrome_fp, ChromeFingerprint)


def test_all_fingerprints(fingerprint_generator: FingerprintGenerator):
    for index in range(10000):
        chrome_fp = fingerprint_generator.get_fingerprint(fingerprint_index=index)
        assert isinstance(chrome_fp, ChromeFingerprint)


def test_threaded_loading():
    start_time = time.time()
    # Load the FingerprintGenerator
    fingerprint_generator = FingerprintGenerator()
    init_time = time.time() - start_time
    # Load a Fingerprint
    fingerprint_generator.get_fingerprint()
    load_time = time.time() - start_time

    # Check if the Fingerprint Load Time is bigger than the Fingerprint Init Time
    # Because the DataLoading is threaded, the Loading should Not Block until a fingerprint is requested
    # Therefore, we can check the threaded loading by checking the Load Times.
    assert load_time > init_time

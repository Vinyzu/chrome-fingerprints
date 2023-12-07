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

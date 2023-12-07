from chrome_fingerprints import FingerprintGenerator

fingerprint_generator = FingerprintGenerator()

errors = 0
for index in range(10000):
    try:
        chrome_fp = fingerprint_generator.get_fingerprint(fingerprint_index=index)
    except Exception as e:
        print(e)
        errors += 1

print(errors)

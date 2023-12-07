# Chrome-Fingerprints v1.0
![Tests & Linting](https://github.com/Vinyzu/chrome-fingerprints/actions/workflows/tests.yml/badge.svg)

#### Chrome-Fingeprints is a dataset of 10k collected Windows Chrome Fingerprints.
#### Usable with an easy-to-use API, available as a compressed (lzma) or full-size Json (view Releases)
#### It uses just two external packages: `OrJson` for faster Json serialization and `DaCite` for dataclass management.


## Install it from PyPI

```bash
pip install chrome-fingerprints
```

---

## Usage

```py
from chrome_fingerprints import FingerprintGenerator, ChromeFingerprint

fp_gen = FingerprintGenerator()

fingerprint: ChromeFingerprint = fp_gen.get_fingerprint()
```
---

## Copyright and License
© [Vinyzu](https://github.com/Vinyzu/)

[GNU GPL](https://choosealicense.com/licenses/gpl-3.0/)

(Commercial Usage is allowed, but source, license and copyright has to made available. Botright does not provide and Liability or Warranty)

---

## Thanks to

[Kaliiiiiiiiii](https://github.com/kaliiiiiiiiii/) (For shared knowledge of Browser automation)

---

![Version](https://img.shields.io/badge/Chrome_Fingerprints-v1.0-blue)
![License](https://img.shields.io/badge/License-GNU%20GPL-green)
![Python](https://img.shields.io/badge/Python-v3.x-lightgrey)

[![my-discord](https://img.shields.io/badge/My_Discord-000?style=for-the-badge&logo=google-chat&logoColor=blue)](https://discordapp.com/users/935224495126487150)
[![buy-me-a-coffee](https://img.shields.io/badge/Buy_Me_A_Coffee-000?style=for-the-badge&logo=ko-fi&logoColor=brown)](https://ko-fi.com/vinyzu)
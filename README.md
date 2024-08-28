# Chrome-Fingerprints v1.1
![Tests & Linting](https://github.com/Vinyzu/chrome-fingerprints/actions/workflows/tests.yml/badge.svg)

#### Chrome-Fingeprints is a dataset of 10k collected Windows Chrome Fingerprints.
#### Usable with an easy-to-use API, available as a compressed (lzma) or full-size Json (view Releases)
#### It uses just three external packages: `OrJson` for faster Json serialization, `DaCite` for dataclass management and `AIOMisc` for async lzma-file reading 

---

## Sponsors
[![Capsolver Banner](https://github.com/user-attachments/assets/b39e70da-3011-4743-9e87-e63947bf41b9)](https://www.capsolver.com/?utm_source=github&utm_medium=banner_github&utm_campaign=botright)

[Capsolver.com](https://www.capsolver.com/?utm_source=github&utm_medium=banner_github&utm_campaign=chrome-fingerprints) is an AI-powered service that specializes in solving various types of captchas automatically. It supports captchas such as [reCAPTCHA V2](https://docs.capsolver.com/guide/captcha/ReCaptchaV2.html?utm_source=github&utm_medium=banner_github&utm_campaign=chrome-fingerprints), [reCAPTCHA V3](https://docs.capsolver.com/guide/captcha/ReCaptchaV3.html?utm_source=github&utm_medium=banner_github&utm_campaign=chrome-fingerprints), [hCaptcha](https://docs.capsolver.com/guide/captcha/HCaptcha.html?utm_source=github&utm_medium=banner_github&utm_campaign=chrome-fingerprints), [FunCaptcha](https://docs.capsolver.com/guide/captcha/FunCaptcha.html?utm_source=github&utm_medium=banner_github&utm_campaign=chrome-fingerprints), [DataDome](https://docs.capsolver.com/guide/captcha/DataDome.html?utm_source=github&utm_medium=banner_github&utm_campaign=chrome-fingerprints), [AWS Captcha](https://docs.capsolver.com/guide/captcha/awsWaf.html?utm_source=github&utm_medium=banner_github&utm_campaign=chrome-fingerprints), [Geetest](https://docs.capsolver.com/guide/captcha/Geetest.html?utm_source=github&utm_medium=banner_github&utm_campaign=chrome-fingerprints), and Cloudflare [Captcha](https://docs.capsolver.com/guide/antibots/cloudflare_turnstile.html?utm_source=github&utm_medium=banner_github&utm_campaign=chrome-fingerprints) / [Challenge 5s](https://docs.capsolver.com/guide/antibots/cloudflare_challenge.html?utm_source=github&utm_medium=banner_github&utm_campaign=chrome-fingerprints), [Imperva / Incapsula](https://docs.capsolver.com/guide/antibots/imperva.html?utm_source=github&utm_medium=banner_github&utm_campaign=chrome-fingerprints), among others.

For developers, Capsolver offers API integration options detailed in their [documentation](https://docs.capsolver.com/?utm_source=github&utm_medium=banner_github&utm_campaign=chrome-fingerprints), facilitating the integration of captcha solving into applications. They also provide browser extensions for [Chrome](https://chromewebstore.google.com/detail/captcha-solver-auto-captc/pgojnojmmhpofjgdmaebadhbocahppod) and [Firefox](https://addons.mozilla.org/es/firefox/addon/capsolver-captcha-solver/), making it easy to use their service directly within a browser. Different pricing packages are available to accommodate varying needs, ensuring flexibility for users.

---

[![Evomi Banner](https://my.evomi.com/images/brand/cta.png)](https://evomi.com?utm_source=github&utm_medium=banner&utm_campaign=Vinyzu-ChromeFingerprints)

**Evomi** is your Swiss Quality, affordable Proxy Provider. I can personally recommend them for their High Quality Residential Proxies.

- 🌍 **Global Presence**: Available in 150+ Countries
- ⚡ **Guaranteed Low Latency**
- 🔒 **Swiss Quality and Privacy**
- 🎁 **Free Trial**: No Credit Card Required
- 🛡️ **99.9% Uptime**
- 🤝 **Special IP Pool selection**: Optimize for fast, quality or quantity of ips
- 🔧 **Easy Integration**: Compatible with most software and programming languages

---

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

## Async Usage

```py
import asyncio

from chrome_fingerprints.fingerprints import AsyncFingerprintGenerator, ChromeFingerprint

async def main():
    fp_gen = AsyncFingerprintGenerator()
    fingerprint: ChromeFingerprint = await fp_gen.get_fingerprint()

if __name__ == '__main__':
    asyncio.run(main())
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

![Version](https://img.shields.io/badge/Chrome_Fingerprints-v1.1-blue)
![License](https://img.shields.io/badge/License-GNU%20GPL-green)
![Python](https://img.shields.io/badge/Python-v3.x-lightgrey)

[![my-discord](https://img.shields.io/badge/My_Discord-000?style=for-the-badge&logo=google-chat&logoColor=blue)](https://discordapp.com/users/935224495126487150)
[![buy-me-a-coffee](https://img.shields.io/badge/Buy_Me_A_Coffee-000?style=for-the-badge&logo=ko-fi&logoColor=brown)](https://ko-fi.com/vinyzu)

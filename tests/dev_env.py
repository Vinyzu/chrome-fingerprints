import asyncio

from chrome_fingerprints.fingerprints import AsyncFingerprintGenerator


async def main():
    fp_gen = AsyncFingerprintGenerator()
    print(await fp_gen.get_fingerprint())

asyncio.run(main())

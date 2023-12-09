import os
import lzma
import random
import asyncio
from concurrent.futures import ThreadPoolExecutor
from typing import List, Dict, Any, Optional

import orjson
import dacite as dataclass_manager
from aiomisc.io import async_open, Compression

from .fingerprint_typing import ChromeFingerprint
from .vars import codecs, keyboard_codes, headers, webgl_extensions, user_agents, voice_uris, fonts


def index_fingerprint(fingerprint) -> None:
    # Codecs
    fingerprint["codecs"] = [codecs[codec_index] for codec_index in fingerprint.get("codecs")]

    # I know that is the worst one-liner ever :(
    for (peer, codec_type) in [("receiver", "video"), ("receiver", "audio"), ("sender", "video"), ("sender", "audio")]:
        # if not fingerprint["webrtc"][peer][codec_type].get("codecs"):
        #     print(fingerprint["webrtc"])

        if isinstance(fingerprint["webrtc"][peer][codec_type]["codecs"], dict):
            new_codecs = {codec[0]: codecs[codec[1]] if codec[0] == "mimeType" else codec[1]
                          for codec in fingerprint["webrtc"][peer][codec_type]["codecs"].items()}
        else:
            new_codecs = fingerprint["webrtc"][peer][codec_type]["codecs"]
        fingerprint["webrtc"][peer][codec_type]["codecs"] = new_codecs

    # Keyboard Codes
    fingerprint["keyboard"] = {key: keyboard_codes[code_index] for (key, code_index) in fingerprint.get("keyboard").items()}

    # Headers
    fingerprint["headers"] = [headers[header_index] for header_index in fingerprint.get("headers")]

    # WebGL Extensions
    fingerprint["webgl"]["extensions"] = [webgl_extensions[extension_index] for extension_index in fingerprint["webgl"].get("extensions")]
    fingerprint["webgl"]["extensions2"] = [webgl_extensions[extension_index] for extension_index in fingerprint["webgl"].get("extensions2")]

    # UserAgent
    fingerprint["navigator"]["user_agent"] = user_agents[fingerprint["navigator"]["user_agent"]]

    # Speech VoiceURIs
    fingerprint["speech"] = [
        {
            "voice_uri": voice_uris[speech_synth.get("voice_uri")],
            "name": voice_uris[speech_synth.get("voice_uri")],
            "lang": speech_synth.get("lang"),
            "local_service": speech_synth.get("local_service"),
            "default": speech_synth.get("default"),
        } for speech_synth in fingerprint.get("speech")
    ]

    # Fonts
    fingerprint["fonts"] = [fonts[font_index] if (isinstance(font_index, int) and font_index < len(fonts)) else font_index for font_index in fingerprint.get("fonts")]


class FingerprintGenerator:
    def __init__(self) -> None:
        self.fingerprints: Optional[List[Dict[str, Any]]] = None

        # Preloading: Fingerprint Decompression & Json Loading takes ~2 seconds
        self.executor = ThreadPoolExecutor(max_workers=1)

        try:
            self.fingerprint_loading_feature = self.executor.submit(self.initialize_fingerprints)
        except Exception as e:
            self.executor.shutdown(wait=True, cancel_futures=True)
            raise e

    def initialize_fingerprints(self) -> None:
        dir_path = os.path.dirname(os.path.realpath(__file__))

        with lzma.open(os.path.join(dir_path, "fingerprints.json.xz"), 'rb') as f:
            json_data = f.read()

        self.fingerprints = orjson.loads(json_data)

    def get_fingerprint(self, fingerprint_index: Optional[int] = None) -> ChromeFingerprint:
        try:
            if not self.fingerprint_loading_feature.done():
                self.fingerprint_loading_feature.result(timeout=10)

            assert self.fingerprints
        except Exception as e:
            self.executor.shutdown(wait=True, cancel_futures=True)
            raise e

        if fingerprint_index:
            fingerprint = self.fingerprints[fingerprint_index]
        else:
            fingerprint = random.choice(self.fingerprints)

        # Check if fingerprint was already loaded
        if not isinstance(fingerprint["navigator"]["user_agent"], str):  # Checking if user agent is not already indexed
            index_fingerprint(fingerprint)

        chrome_fp = dataclass_manager.from_dict(ChromeFingerprint, fingerprint)
        return chrome_fp


class AsyncFingerprintGenerator:
    def __init__(self):
        self.fingerprints: Optional[List[Dict[str, Any]]] = None

        loop = asyncio.get_running_loop()
        self.fingerprint_loading_feature = loop.create_task(self.initialize_fingerprints())

    async def initialize_fingerprints(self) -> None:
        dir_path = os.path.dirname(os.path.realpath(__file__))

        async with async_open(os.path.join(dir_path, "fingerprints.json.xz"), 'rb', compression=Compression.LZMA) as f:
            json_data = await f.read()

        self.fingerprints = orjson.loads(json_data)

    async def get_fingerprint(self, fingerprint_index: Optional[int] = None) -> ChromeFingerprint:
        if not self.fingerprint_loading_feature.done():
            await self.fingerprint_loading_feature

        assert self.fingerprints

        if fingerprint_index:
            fingerprint = self.fingerprints[fingerprint_index]
        else:
            fingerprint = random.choice(self.fingerprints)

        # Check if fingerprint was already loaded
        if not isinstance(fingerprint["navigator"]["user_agent"], str):  # Checking if user agent is not already indexed
            index_fingerprint(fingerprint)

        chrome_fp = dataclass_manager.from_dict(ChromeFingerprint, fingerprint)
        return chrome_fp

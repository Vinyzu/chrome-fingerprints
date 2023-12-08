import os
from typing import List, Dict, Any, Optional
import lzma
import threading
import time
import random

import orjson
import dacite as dataclass_manager

from .fingerprint_typing import ChromeFingerprint
from .vars import codecs, keyboard_codes, headers, webgl_extensions, user_agents, voice_uris, fonts


class FingerprintGenerator:
    def __init__(self) -> None:
        self.fingerprints: Optional[List[Dict[str, Any]]] = None

        # Preloading: Fingerprint Decompression & Json Loading takes ~2 seconds
        self.initialize_fingerprints()

    def initialize_fingerprints(self) -> None:
        dir_path = os.path.dirname(os.path.realpath(__file__))

        with lzma.open(os.path.join(dir_path, "fingerprints.json.xz"), 'rb') as f:
            json_data = f.read()

        self.fingerprints = orjson.loads(json_data)

    def get_fingerprint(self, fingerprint_index: Optional[int] = None) -> ChromeFingerprint:
        assert self.fingerprints

        if fingerprint_index:
            fingerprint = self.fingerprints[fingerprint_index]
        else:
            fingerprint = random.choice(self.fingerprints)

        self.index_fingerprint(fingerprint)
        self.extend_fingerprint(fingerprint)

        chrome_fp = dataclass_manager.from_dict(ChromeFingerprint, fingerprint)
        return chrome_fp

    @staticmethod
    def index_fingerprint(fingerprint) -> None:
        # Codecs
        fingerprint["codecs"] = [codecs[codec_index] if isinstance(codec_index, int) else codec_index for codec_index in fingerprint.get("codecs")]

        # I know that is the worst one-liner ever :(
        for (peer, codec_type) in [("receiver", "video"), ("receiver", "audio"), ("sender", "video"), ("sender", "audio")]:
            # if not fingerprint["webrtc"][peer][codec_type].get("codecs"):
            #     print(fingerprint["webrtc"])

            if isinstance(fingerprint["webrtc"][peer][codec_type]["codecs"], dict):
                new_codecs = {codec[0]: codecs[codec[1]] if (codec[0] == "mimeType" and isinstance(codec[1], int)) else codec[1]
                              for codec in fingerprint["webrtc"][peer][codec_type]["codecs"].items()}
            else:
                new_codecs = fingerprint["webrtc"][peer][codec_type]["codecs"]
            fingerprint["webrtc"][peer][codec_type]["codecs"] = new_codecs

        # Keyboard Codes
        fingerprint["keyboard"] = {key: keyboard_codes[code_index] if isinstance(code_index, int) else code_index for (key, code_index) in fingerprint.get("keyboard").items()}

        # Headers
        fingerprint["headers"] = [headers[header_index] if isinstance(header_index, int) else header_index for header_index in fingerprint.get("headers")]

        # WebGL Extensions
        fingerprint["webgl"]["extensions"] = [webgl_extensions[extension_index] if isinstance(extension_index, int) else extension_index for extension_index in fingerprint["webgl"].get("extensions")]
        fingerprint["webgl"]["extensions2"] = [webgl_extensions[extension_index] if isinstance(extension_index, int) else extension_index for extension_index in
                                               fingerprint["webgl"].get("extensions2")]

        # UserAgent
        fingerprint["navigator"]["user_agent"] = user_agents[fingerprint["navigator"]["user_agent"]] \
            if isinstance(fingerprint["navigator"]["user_agent"], int) else fingerprint["navigator"]["user_agent"]

        # Speech VoiceURIs
        fingerprint["speech"] = [
            {
                "voice_uri": voice_uris[speech_synth.get("voice_uri")] if isinstance(speech_synth.get("voice_uri"), int) else speech_synth.get("voice_uri"),
                "name": voice_uris[speech_synth.get("voice_uri")] if isinstance(speech_synth.get("voice_uri"), int) else speech_synth.get("voice_uri"),
                "lang": speech_synth.get("lang"),
                "local_service": speech_synth.get("local_service"),
                "default": speech_synth.get("default"),
            } for speech_synth in fingerprint.get("speech")
        ]

        # Fonts
        fingerprint["fonts"] = [fonts[font_index] if (isinstance(font_index, int) and font_index < len(fonts)) else font_index for font_index in fingerprint.get("fonts")]

    @staticmethod
    def extend_fingerprint(fingerprint) -> None:
        # Navigator AppVersion
        fingerprint["navigator"]["app_version"] = fingerprint["navigator"]["user_agent"].split("/")[1]

        # Navigator Brands
        fingerprint["navigator"]["brands"] = [
            {"brand": brand["brand"], "version": brand["version"].split(".")[0]}
            for brand in fingerprint["navigator"]["full_version_list"]
        ]

class AsyncFingerprintGenerator(FingerprintGenerator):
   def __init__(self):
      self.fingerprints: Optional[List[Dict[str, Any]]] = None
       
   def __await__(self):
       return self._ainit.__await__()

   async def _ainit(self):
       loop = asyncio.get_running_loop()
       await loop.run_in_executor(None, self.initialize_fingerprints)

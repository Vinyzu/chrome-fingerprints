from dataclasses import dataclass
from typing import Dict, List, Any, Optional


@dataclass
class NavigatorPlatform:
    name: str
    version: str
    architecture: str
    model: str
    bitness: str
    wow64: bool


@dataclass(unsafe_hash=True)
class Navigator:
    user_agent: str
    app_version: str
    app_codename: str
    app_name: str
    product: str
    product_sub: str
    vendor: str
    vendor_sub: str
    pdf_viewer_enabled: bool
    full_version: str
    full_version_list: List[Dict[str, str]]
    brands: List[Dict[str, str]]
    platform: NavigatorPlatform


@dataclass
class Screen:
    avail_height: int
    avail_width: int
    width: int
    height: int
    color_depth: int
    pixel_depth: int
    avail_left: int
    avail_top: int
    device_pixel_ratio: float


@dataclass
class Plugin:
    name: str
    file_name: str
    description: str
    ref: int
    mimes: List[int]


@dataclass
class SpeechSynth:
    voice_uri: str
    name: str
    lang: str
    local_service: bool
    default: bool


@dataclass(unsafe_hash=True)
class WebGL:
    vendor: str
    renderer: str
    unmasked_vendor: str
    unmasked_renderer: str
    shading_language: str
    shading_language2: Optional[str]
    version: str
    version2: Optional[str]
    max_anisotropy: str
    extensions: List[str]
    extensions2: List[str]
    properties: Dict[str, str | int | float | bool | dict | list]  # type: ignore


@dataclass
class WebGPUPerformanceInfo:
    vendor: str
    architecture: str
    device: str
    description: str


# @dataclass(unsafe_hash=True)
# class WebGPUPerformance:
#     is_fallback_adapter: bool
#     features: List[str]  # Optional[List[str]]
#     info: WebGPUPerformanceInfo  # Optional[WebGPUPerformanceInfo]
#     limits: Dict[str, str]  # Optional[Dict[str, str]]


# @dataclass(unsafe_hash=True)
# class WebGPU:
#     enabled: bool
#     fallback: Optional[bool]
#     preferred_canvas_format: str  # Optional[str]
#
#     high_performance: WebGPUPerformance
#     low_performance: WebGPUPerformance


@dataclass(unsafe_hash=True)
class WebRTCPeerType:
    codecs: Any
    extensions: Any


@dataclass(unsafe_hash=True)
class WebRTCPeer:
    video: WebRTCPeerType
    audio: WebRTCPeerType


@dataclass(unsafe_hash=True)
class WebRTC:
    receiver: WebRTCPeer
    sender: WebRTCPeer


@dataclass(unsafe_hash=True)
class ChromeFingerprint:
    hardware_concurrency: int
    device_memory: float
    do_not_track: bool
    hls_enabled: bool

    navigator: Navigator
    screen: Screen
    plugins: List[Plugin]
    speech: List[SpeechSynth]
    webgl: WebGL
    # webgpu: WebGPU
    webrtc: WebRTC

    fonts: List[str | int]
    codecs: List[str]
    headers: List[str]
    keyboard: Dict[str, str]
    css: Dict[str, str | int]
    audio: Dict[str, Optional[str | int | float]]

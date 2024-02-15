"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""


import requests as requests_http
from .utils import utils
from .utils.retries import RetryConfig
from dataclasses import dataclass
from typing import Dict, Tuple


SERVERS = [
    'https://api.wingspan.app',
    # Wingspan's Payments API in Production
    'https://stagingapi.wingspan.app',
    # Wingspan's Payments API in Staging
]
"""Contains the list of servers available to the SDK"""

@dataclass
class SDKConfiguration:
    client: requests_http.Session
    server_url: str = ''
    server_idx: int = 0
    language: str = 'python'
    openapi_doc_version: str = '1.0.0'
    sdk_version: str = '5.0.1'
    gen_version: str = '2.258.0'
    user_agent: str = 'speakeasy-sdk/python 5.0.1 2.258.0 1.0.0 wingspan'
    retry_config: RetryConfig = None

    def get_server_details(self) -> Tuple[str, Dict[str, str]]:
        if self.server_url:
            return utils.remove_suffix(self.server_url, '/'), {}
        if self.server_idx is None:
            self.server_idx = 0

        return SERVERS[self.server_idx], {}

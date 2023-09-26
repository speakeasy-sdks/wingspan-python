"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import calculate1099response as shared_calculate1099response
from typing import Optional



@dataclasses.dataclass
class Calculate1099Response:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    calculate1099_response: Optional[shared_calculate1099response.Calculate1099Response] = dataclasses.field(default=None)
    r"""Calculate 1099 amounts response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    


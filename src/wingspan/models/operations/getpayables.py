"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import payablessummary as shared_payablessummary
from typing import Optional


@dataclasses.dataclass
class GetPayablesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    payables_summary: Optional[shared_payablessummary.PayablesSummary] = dataclasses.field(default=None)
    r"""A payables summary, with current payables numbers"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    


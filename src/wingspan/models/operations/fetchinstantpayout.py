"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import instantpayoutresponse as shared_instantpayoutresponse
from typing import Optional


@dataclasses.dataclass
class FetchInstantPayoutResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    instant_payout_response: Optional[shared_instantpayoutresponse.InstantPayoutResponse] = dataclasses.field(default=None)
    r"""Instant Payout details"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    


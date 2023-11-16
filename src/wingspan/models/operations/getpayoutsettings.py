"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import payoutsettingsresponse as shared_payoutsettingsresponse
from typing import Optional


@dataclasses.dataclass
class GetPayoutSettingsRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique identifier"""
    



@dataclasses.dataclass
class GetPayoutSettingsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    payout_settings_response: Optional[shared_payoutsettingsresponse.PayoutSettingsResponse] = dataclasses.field(default=None)
    r"""The payout settings for a member"""
    


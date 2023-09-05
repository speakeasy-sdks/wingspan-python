"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import payoutsettingsresponse as shared_payoutsettingsresponse
from ..shared import payoutsettingsupdate as shared_payoutsettingsupdate
from typing import Optional



@dataclasses.dataclass
class UpdatePayoutSettingsRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique identifier"""
    payout_settings_update: Optional[shared_payoutsettingsupdate.PayoutSettingsUpdate] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    




@dataclasses.dataclass
class UpdatePayoutSettingsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    payout_settings_response: Optional[shared_payoutsettingsresponse.PayoutSettingsResponse] = dataclasses.field(default=None)
    r"""The payout settings for a member"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

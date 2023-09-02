"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import checkbookcard as shared_checkbookcard
from typing import Optional



@dataclasses.dataclass
class GetPaymentsPayoutSettingsMemberIDDebitCardRequest:
    member_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'memberId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier of a member"""
    




@dataclasses.dataclass
class GetPaymentsPayoutSettingsMemberIDDebitCardResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    checkbook_cards: Optional[list[shared_checkbookcard.CheckbookCard]] = dataclasses.field(default=None)
    r"""A list of payout debit cards"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

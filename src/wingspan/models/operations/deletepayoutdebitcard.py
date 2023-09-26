"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import checkbookcard as shared_checkbookcard
from typing import Optional



@dataclasses.dataclass
class DeletePayoutDebitCardRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique identifier"""
    member_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'memberId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier of a member"""
    




@dataclasses.dataclass
class DeletePayoutDebitCardResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    checkbook_card: Optional[shared_checkbookcard.CheckbookCard] = dataclasses.field(default=None)
    r"""A payout debit card"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    


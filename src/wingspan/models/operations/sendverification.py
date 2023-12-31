"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import cardcoderequest as shared_cardcoderequest
from ..shared import cardcoderesponse as shared_cardcoderesponse
from typing import Optional


@dataclasses.dataclass
class SendVerificationRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique identifier"""
    card_code_request: Optional[shared_cardcoderequest.CardCodeRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class SendVerificationResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    card_code_response: Optional[shared_cardcoderesponse.CardCodeResponse] = dataclasses.field(default=None)
    r"""A card code response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    


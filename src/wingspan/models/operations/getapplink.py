"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import bankingapplicationform as shared_bankingapplicationform
from typing import Optional


@dataclasses.dataclass
class GetAppLinkRequest:
    member_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'memberId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier of a member"""
    



@dataclasses.dataclass
class GetAppLinkResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    banking_application_form: Optional[shared_bankingapplicationform.BankingApplicationForm] = dataclasses.field(default=None)
    r"""A Bank Application form"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    


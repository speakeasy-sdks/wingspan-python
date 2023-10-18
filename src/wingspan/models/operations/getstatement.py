"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import bankstatement as shared_bankstatement
from typing import List, Optional


@dataclasses.dataclass
class GetStatementRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique identifier"""
    



@dataclasses.dataclass
class GetStatementResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    bank_statements: Optional[List[shared_bankstatement.BankStatement]] = dataclasses.field(default=None)
    r"""A list of bank statements"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    


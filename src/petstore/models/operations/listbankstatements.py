"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import bankstatement as shared_bankstatement
from typing import Optional



@dataclasses.dataclass
class ListBankStatementsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    bank_statements: Optional[list[shared_bankstatement.BankStatement]] = dataclasses.field(default=None)
    r"""A list of bank statements"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    


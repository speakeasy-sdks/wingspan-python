"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import memberclientschema as shared_memberclientschema
from typing import Optional



@dataclasses.dataclass
class CreateMemberClientResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    member_client_schema: Optional[shared_memberclientschema.MemberClientSchema] = dataclasses.field(default=None)
    r"""Describes details of member and client"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    


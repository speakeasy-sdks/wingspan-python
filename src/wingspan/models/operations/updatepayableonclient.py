"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import payableschema as shared_payableschema
from ..shared import payableupdaterequest as shared_payableupdaterequest
from typing import Optional



@dataclasses.dataclass
class UpdatePayableOnClientRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique identifier"""
    payable_update_request: Optional[shared_payableupdaterequest.PayableUpdateRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    




@dataclasses.dataclass
class UpdatePayableOnClientResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    payable_schema: Optional[shared_payableschema.PayableSchema] = dataclasses.field(default=None)
    r"""A payable"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

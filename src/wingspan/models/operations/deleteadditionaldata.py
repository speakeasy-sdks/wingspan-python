"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import additionaldata as shared_additionaldata
from typing import Optional



@dataclasses.dataclass
class DeleteAdditionalDataRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique identifier"""
    




@dataclasses.dataclass
class DeleteAdditionalDataResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    additional_data: Optional[shared_additionaldata.AdditionalData] = dataclasses.field(default=None)
    r"""Custom fields that are set on memberClient object to describe collaborator-member"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

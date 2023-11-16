"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import additionaldata as shared_additionaldata
from ...models.shared import additionaldataupdaterequest as shared_additionaldataupdaterequest
from typing import Optional


@dataclasses.dataclass
class UpdateAdditionalSettingsRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique identifier"""
    additional_data_update_request: Optional[shared_additionaldataupdaterequest.AdditionalDataUpdateRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class UpdateAdditionalSettingsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    additional_data: Optional[shared_additionaldata.AdditionalData] = dataclasses.field(default=None)
    r"""Custom fields that are set on memberClient object to describe collaborator-member"""
    


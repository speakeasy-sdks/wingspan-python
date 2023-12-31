"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import collaboratorv2 as shared_collaboratorv2
from typing import Optional


@dataclasses.dataclass
class GetCollaboratorV2Request:
    member_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'memberId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier of a member"""
    



@dataclasses.dataclass
class GetCollaboratorV2Response:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    collaborator_v2: Optional[shared_collaboratorv2.CollaboratorV2] = dataclasses.field(default=None)
    r"""A single V2 Collaborator"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    


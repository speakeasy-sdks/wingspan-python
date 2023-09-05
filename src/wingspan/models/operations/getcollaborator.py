"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import collaboratorschema as shared_collaboratorschema
from typing import Optional



@dataclasses.dataclass
class GetCollaboratorRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique identifier"""
    




@dataclasses.dataclass
class GetCollaboratorResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    collaborator_schema: Optional[shared_collaboratorschema.CollaboratorSchema] = dataclasses.field(default=None)
    r"""A collaborator is a contractor that can receive payments"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    


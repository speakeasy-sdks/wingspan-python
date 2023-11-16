"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import collaboratorschema as shared_collaboratorschema
from ...models.shared import collaboratorupdaterequest as shared_collaboratorupdaterequest
from typing import Optional


@dataclasses.dataclass
class UpdateCollaboratorRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique identifier"""
    collaborator_update_request: Optional[shared_collaboratorupdaterequest.CollaboratorUpdateRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class UpdateCollaboratorResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    collaborator_schema: Optional[shared_collaboratorschema.CollaboratorSchema] = dataclasses.field(default=None)
    r"""A collaborator is a contractor that can receive payments"""
    


"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import collaboratorv2 as shared_collaboratorv2
from typing import List, Optional


@dataclasses.dataclass
class ListClientCollaboratorsV2Response:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    classes: Optional[List[shared_collaboratorv2.CollaboratorV2]] = dataclasses.field(default=None)
    r"""List of V2 Collaborators"""
    


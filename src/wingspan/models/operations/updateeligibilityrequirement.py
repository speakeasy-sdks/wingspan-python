"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import eligibilityrequirement as shared_eligibilityrequirement
from ...models.shared import eligibilityrequirementupdaterequest as shared_eligibilityrequirementupdaterequest
from typing import List, Optional


@dataclasses.dataclass
class UpdateEligibilityRequirementRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique identifier"""
    eligibility_requirement_update_request: Optional[shared_eligibilityrequirementupdaterequest.EligibilityRequirementUpdateRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class UpdateEligibilityRequirementResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    classes: Optional[List[shared_eligibilityrequirement.EligibilityRequirement]] = dataclasses.field(default=None)
    r"""List of Eligibility Requirements"""
    


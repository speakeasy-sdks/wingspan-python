"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import eligibilityrequirement as shared_eligibilityrequirement
from typing import List, Optional


@dataclasses.dataclass
class GetEligibilityRequirementRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique identifier"""
    



@dataclasses.dataclass
class GetEligibilityRequirementResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    eligibility_requirements: Optional[List[shared_eligibilityrequirement.EligibilityRequirement]] = dataclasses.field(default=None)
    r"""List of Eligibility Requirements"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    


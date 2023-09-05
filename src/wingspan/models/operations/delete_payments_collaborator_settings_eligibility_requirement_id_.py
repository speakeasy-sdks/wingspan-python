"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import eligibilityrequirement as shared_eligibilityrequirement
from typing import Optional



@dataclasses.dataclass
class DeletePaymentsCollaboratorSettingsEligibilityRequirementIDRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique identifier"""
    




@dataclasses.dataclass
class DeletePaymentsCollaboratorSettingsEligibilityRequirementIDResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    eligibility_requirements: Optional[list[shared_eligibilityrequirement.EligibilityRequirement]] = dataclasses.field(default=None)
    r"""List of Eligibility Requirements"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    


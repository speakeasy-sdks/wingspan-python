"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import eligibilityrequirement as shared_eligibilityrequirement
from typing import Optional



@dataclasses.dataclass
class CreateEligibilityRequirementResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    eligibility_requirement: Optional[shared_eligibilityrequirement.EligibilityRequirement] = dataclasses.field(default=None)
    r"""Eligibility Requirement"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    


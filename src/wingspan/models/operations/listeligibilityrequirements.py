"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import eligibilityrequirement as shared_eligibilityrequirement
from typing import List, Optional


@dataclasses.dataclass
class ListEligibilityRequirementsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    classes: Optional[List[shared_eligibilityrequirement.EligibilityRequirement]] = dataclasses.field(default=None)
    r"""List of Eligibility Requirements"""
    


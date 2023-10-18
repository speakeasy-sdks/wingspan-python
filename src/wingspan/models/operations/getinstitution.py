"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import institutionresponse as shared_institutionresponse
from typing import Optional


@dataclasses.dataclass
class GetInstitutionRequest:
    routing_number: str = dataclasses.field(metadata={'path_param': { 'field_name': 'routingNumber', 'style': 'simple', 'explode': False }})
    r"""Bank Routing Number"""
    



@dataclasses.dataclass
class GetInstitutionResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    institution_response: Optional[shared_institutionresponse.InstitutionResponse] = dataclasses.field(default=None)
    r"""Institution Response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    


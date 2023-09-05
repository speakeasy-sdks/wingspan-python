"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import deductionresponse as shared_deductionresponse
from typing import Optional



@dataclasses.dataclass
class ListClientDeductionsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    deduction_responses: Optional[list[shared_deductionresponse.DeductionResponse]] = dataclasses.field(default=None)
    r"""A list of deductions"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

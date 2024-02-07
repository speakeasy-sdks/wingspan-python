"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import deductionresponse as shared_deductionresponse
from typing import List, Optional


@dataclasses.dataclass
class ListClientDeductionsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    classes: Optional[List[shared_deductionresponse.DeductionResponse]] = dataclasses.field(default=None)
    r"""A list of deductions"""
    


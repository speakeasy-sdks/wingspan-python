"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import bulkcalculation1099batch as shared_bulkcalculation1099batch
from typing import List, Optional


@dataclasses.dataclass
class ListBulkCalculation1099BatchesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    classes: Optional[List[shared_bulkcalculation1099batch.BulkCalculation1099Batch]] = dataclasses.field(default=None)
    r"""A list of bulk calculation 1099 batches"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    


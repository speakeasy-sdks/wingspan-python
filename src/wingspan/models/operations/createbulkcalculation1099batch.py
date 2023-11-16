"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import bulkcalculation1099batch as shared_bulkcalculation1099batch
from typing import Optional


@dataclasses.dataclass
class CreateBulkCalculation1099BatchResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    bulk_calculation1099_batch: Optional[shared_bulkcalculation1099batch.BulkCalculation1099Batch] = dataclasses.field(default=None)
    r"""A batch of items for importing as calculation 1099s"""
    


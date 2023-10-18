"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import bulkpayableimportsummary as shared_bulkpayableimportsummary
from typing import Optional


@dataclasses.dataclass
class GetBulkPayableBatchSummaryRequest:
    batch_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'batchId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a batch"""
    



@dataclasses.dataclass
class GetBulkPayableBatchSummaryResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    bulk_payable_import_summary: Optional[shared_bulkpayableimportsummary.BulkPayableImportSummary] = dataclasses.field(default=None)
    r"""Summary of the bulk payable import"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    


"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import bulkinvoicebatch as shared_bulkinvoicebatch
from typing import List, Optional


@dataclasses.dataclass
class ListBulkInvoiceBatchesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    bulk_invoice_batches: Optional[List[shared_bulkinvoicebatch.BulkInvoiceBatch]] = dataclasses.field(default=None)
    r"""A list of bulk invoice batches"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    


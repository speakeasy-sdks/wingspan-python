"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import bulkinvoicebatch as shared_bulkinvoicebatch
from typing import Optional



@dataclasses.dataclass
class CreateBulkInvoiceBatchResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    bulk_invoice_batch: Optional[shared_bulkinvoicebatch.BulkInvoiceBatch] = dataclasses.field(default=None)
    r"""A batch of items for importing as invoices"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    


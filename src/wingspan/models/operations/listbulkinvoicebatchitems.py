"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import bulkinvoiceitem as shared_bulkinvoiceitem
from typing import Optional



@dataclasses.dataclass
class ListBulkInvoiceBatchItemsRequest:
    batch_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'batchId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a batch"""
    




@dataclasses.dataclass
class ListBulkInvoiceBatchItemsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    bulk_invoice_items: Optional[list[shared_bulkinvoiceitem.BulkInvoiceItem]] = dataclasses.field(default=None)
    r"""A list of bulk invoice items"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import bulkinvoiceitem as shared_bulkinvoiceitem
from typing import Optional



@dataclasses.dataclass
class GetBulkInvoiceBatchItemRequest:
    batch_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'batchId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a batch"""
    batch_item_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'batchItemId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for an item in a batch"""
    




@dataclasses.dataclass
class GetBulkInvoiceBatchItemResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    bulk_invoice_item: Optional[shared_bulkinvoiceitem.BulkInvoiceItem] = dataclasses.field(default=None)
    r"""An item that will be converted into a invoice"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

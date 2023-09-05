"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import bulkpayableitem as shared_bulkpayableitem
from ..shared import bulkpayableitemcreate as shared_bulkpayableitemcreate
from typing import Optional



@dataclasses.dataclass
class CreateBulkPayableBatchItemRequest:
    batch_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'batchId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a batch"""
    bulk_payable_item_create: Optional[shared_bulkpayableitemcreate.BulkPayableItemCreate] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    




@dataclasses.dataclass
class CreateBulkPayableBatchItemResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    bulk_payable_item: Optional[shared_bulkpayableitem.BulkPayableItem] = dataclasses.field(default=None)
    r"""An item that will be converted into a payable"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    


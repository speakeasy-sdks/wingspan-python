"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import bulkpayableitem as shared_bulkpayableitem
from typing import Optional


@dataclasses.dataclass
class GetBulkPayableBatchItemRequest:
    batch_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'batchId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a batch"""
    batch_item_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'batchItemId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for an item in a batch"""
    



@dataclasses.dataclass
class GetBulkPayableBatchItemResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    bulk_payable_item: Optional[shared_bulkpayableitem.BulkPayableItem] = dataclasses.field(default=None)
    r"""An item that will be converted into a payable"""
    


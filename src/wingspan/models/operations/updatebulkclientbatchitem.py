"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import bulkclientitem as shared_bulkclientitem
from ..shared import bulkclientitemupdate as shared_bulkclientitemupdate
from typing import Optional


@dataclasses.dataclass
class UpdateBulkClientBatchItemRequest:
    batch_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'batchId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a batch"""
    batch_item_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'batchItemId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for an item in a batch"""
    bulk_client_item_update: Optional[shared_bulkclientitemupdate.BulkClientItemUpdate] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class UpdateBulkClientBatchItemResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    bulk_client_item: Optional[shared_bulkclientitem.BulkClientItem] = dataclasses.field(default=None)
    r"""An item that will be converted into a client"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    


"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import bulkclientitem as shared_bulkclientitem
from ..shared import bulkclientitemcreate as shared_bulkclientitemcreate
from typing import Optional


@dataclasses.dataclass
class CreateBulkClientBatchItemRequest:
    batch_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'batchId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a batch"""
    bulk_client_item_create: Optional[shared_bulkclientitemcreate.BulkClientItemCreate] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class CreateBulkClientBatchItemResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    bulk_client_item: Optional[shared_bulkclientitem.BulkClientItem] = dataclasses.field(default=None)
    r"""An item that will be converted into a client"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    


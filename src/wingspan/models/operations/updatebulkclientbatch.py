"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import bulkbatchupdate as shared_bulkbatchupdate
from ..shared import bulkclientbatch as shared_bulkclientbatch
from typing import Optional



@dataclasses.dataclass
class UpdateBulkClientBatchRequest:
    batch_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'batchId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a batch"""
    bulk_batch_update: Optional[shared_bulkbatchupdate.BulkBatchUpdate] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    




@dataclasses.dataclass
class UpdateBulkClientBatchResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    bulk_client_batch: Optional[shared_bulkclientbatch.BulkClientBatch] = dataclasses.field(default=None)
    r"""A batch of items for importing as clients"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    


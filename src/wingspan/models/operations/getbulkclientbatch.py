"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import bulkclientbatch as shared_bulkclientbatch
from typing import Optional


@dataclasses.dataclass
class GetBulkClientBatchRequest:
    batch_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'batchId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a batch"""
    



@dataclasses.dataclass
class GetBulkClientBatchResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    bulk_client_batch: Optional[shared_bulkclientbatch.BulkClientBatch] = dataclasses.field(default=None)
    r"""A batch of items for importing as clients"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    


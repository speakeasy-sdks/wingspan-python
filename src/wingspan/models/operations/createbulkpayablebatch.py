"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import bulkpayablebatch as shared_bulkpayablebatch
from typing import Optional


@dataclasses.dataclass
class CreateBulkPayableBatchResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    bulk_payable_batch: Optional[shared_bulkpayablebatch.BulkPayableBatch] = dataclasses.field(default=None)
    r"""A batch of items for importing as payables"""
    


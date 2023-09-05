"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import bulkpayablebatch as shared_bulkpayablebatch
from typing import Optional



@dataclasses.dataclass
class ListBulkPayableBatchesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    bulk_payable_batches: Optional[list[shared_bulkpayablebatch.BulkPayableBatch]] = dataclasses.field(default=None)
    r"""A list of bulk payable batches"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    


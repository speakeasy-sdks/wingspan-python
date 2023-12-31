"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import bulkcalculation1099item as shared_bulkcalculation1099item
from typing import List, Optional


@dataclasses.dataclass
class ListBulkCalculation1099BatchItemsRequest:
    batch_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'batchId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a batch"""
    



@dataclasses.dataclass
class ListBulkCalculation1099BatchItemsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    bulk_calculation1099_items: Optional[List[shared_bulkcalculation1099item.BulkCalculation1099Item]] = dataclasses.field(default=None)
    r"""A list of bulk calculation 1099 items"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    


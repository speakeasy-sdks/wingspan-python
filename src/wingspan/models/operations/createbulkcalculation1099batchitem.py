"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import bulkcalculation1099item as shared_bulkcalculation1099item
from ..shared import bulkcalculation1099itemcreate as shared_bulkcalculation1099itemcreate
from typing import Optional



@dataclasses.dataclass
class CreateBulkCalculation1099BatchItemRequest:
    batch_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'batchId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a batch"""
    bulk_calculation1099_item_create: Optional[shared_bulkcalculation1099itemcreate.BulkCalculation1099ItemCreate] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    




@dataclasses.dataclass
class CreateBulkCalculation1099BatchItemResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    bulk_calculation1099_item: Optional[shared_bulkcalculation1099item.BulkCalculation1099Item] = dataclasses.field(default=None)
    r"""An item that will be converted into a calculation 1099"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    


"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import bulkcollaboratoritem as shared_bulkcollaboratoritem
from ..shared import bulkcollaboratoritemcreate as shared_bulkcollaboratoritemcreate
from typing import Optional



@dataclasses.dataclass
class CreateBulkCollaboratorBatchItemRequest:
    batch_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'batchId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a batch"""
    bulk_collaborator_item_create: Optional[shared_bulkcollaboratoritemcreate.BulkCollaboratorItemCreate] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    




@dataclasses.dataclass
class CreateBulkCollaboratorBatchItemResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    bulk_collaborator_item: Optional[shared_bulkcollaboratoritem.BulkCollaboratorItem] = dataclasses.field(default=None)
    r"""An item that will be converted into a collaborator"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

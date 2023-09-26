"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import bulkcollaboratoritem as shared_bulkcollaboratoritem
from ..shared import bulkcollaboratoritemupdate as shared_bulkcollaboratoritemupdate
from typing import Optional



@dataclasses.dataclass
class UpdateBulkCollaboratorBatchItemRequest:
    batch_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'batchId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a batch"""
    batch_item_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'batchItemId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for an item in a batch"""
    bulk_collaborator_item_update: Optional[shared_bulkcollaboratoritemupdate.BulkCollaboratorItemUpdate] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    




@dataclasses.dataclass
class UpdateBulkCollaboratorBatchItemResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    bulk_collaborator_item: Optional[shared_bulkcollaboratoritem.BulkCollaboratorItem] = dataclasses.field(default=None)
    r"""An item that will be converted into a collaborator"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    


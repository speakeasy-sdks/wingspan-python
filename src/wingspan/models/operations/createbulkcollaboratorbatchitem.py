"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import bulkcollaboratoritem as shared_bulkcollaboratoritem
from ...models.shared import bulkcollaboratoritemcreate as shared_bulkcollaboratoritemcreate
from typing import Optional


@dataclasses.dataclass
class CreateBulkCollaboratorBatchItemRequest:
    batch_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'batchId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a batch"""
    bulk_collaborator_item_create: Optional[shared_bulkcollaboratoritemcreate.BulkCollaboratorItemCreate] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class CreateBulkCollaboratorBatchItemResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    bulk_collaborator_item: Optional[shared_bulkcollaboratoritem.BulkCollaboratorItem] = dataclasses.field(default=None)
    r"""An item that will be converted into a collaborator"""
    


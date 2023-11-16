"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import bulkcollaboratorbatch as shared_bulkcollaboratorbatch
from typing import Optional


@dataclasses.dataclass
class GetBulkCollaboratorBatchRequest:
    batch_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'batchId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a batch"""
    



@dataclasses.dataclass
class GetBulkCollaboratorBatchResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    bulk_collaborator_batch: Optional[shared_bulkcollaboratorbatch.BulkCollaboratorBatch] = dataclasses.field(default=None)
    r"""A batch of items for importing as collaborators"""
    


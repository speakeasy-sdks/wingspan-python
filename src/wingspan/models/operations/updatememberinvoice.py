"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import invoice as shared_invoice
from ...models.shared import invoiceupdaterequest as shared_invoiceupdaterequest
from typing import Optional


@dataclasses.dataclass
class UpdateMemberInvoiceRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique identifier"""
    invoice_update_request: Optional[shared_invoiceupdaterequest.InvoiceUpdateRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class UpdateMemberInvoiceResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    invoice: Optional[shared_invoice.Invoice] = dataclasses.field(default=None)
    r"""An invoice"""
    


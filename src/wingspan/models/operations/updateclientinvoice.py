"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import clientinvoice as shared_clientinvoice
from ..shared import clientinvoiceupdaterequest as shared_clientinvoiceupdaterequest
from typing import Optional



@dataclasses.dataclass
class UpdateClientInvoiceRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique identifier"""
    client_invoice_update_request: Optional[shared_clientinvoiceupdaterequest.ClientInvoiceUpdateRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    




@dataclasses.dataclass
class UpdateClientInvoiceResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    client_invoice: Optional[shared_clientinvoice.ClientInvoice] = dataclasses.field(default=None)
    r"""A client created invoice"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

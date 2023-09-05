"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import clientinvoice as shared_clientinvoice
from typing import Optional



@dataclasses.dataclass
class CreateClientInvoiceFeesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    client_invoice: Optional[shared_clientinvoice.ClientInvoice] = dataclasses.field(default=None)
    r"""A client created invoice"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

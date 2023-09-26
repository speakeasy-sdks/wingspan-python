"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import clientinvoicetemplate as shared_clientinvoicetemplate
from typing import Optional



@dataclasses.dataclass
class CreateClientInvoiceTemplateResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    client_invoice_template: Optional[shared_clientinvoicetemplate.ClientInvoiceTemplate] = dataclasses.field(default=None)
    r"""A client created invoiceTemplate (recurring Invoice)"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    


"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import invoicetemplate as shared_invoicetemplate
from typing import Optional


@dataclasses.dataclass
class CreateInvoiceTemplateResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    invoice_template: Optional[shared_invoicetemplate.InvoiceTemplate] = dataclasses.field(default=None)
    r"""A recurring invoice"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    


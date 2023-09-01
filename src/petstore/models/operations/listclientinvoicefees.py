"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import invoicefeecalculation as shared_invoicefeecalculation
from typing import Optional



@dataclasses.dataclass
class ListClientInvoiceFeesRequest:
    invoice_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'invoice_id', 'style': 'simple', 'explode': False }})
    r"""Unique identifier of an invoice"""
    




@dataclasses.dataclass
class ListClientInvoiceFeesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    invoice_fee_calculation: Optional[shared_invoicefeecalculation.InvoiceFeeCalculation] = dataclasses.field(default=None)
    r"""Fees on Invoice"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    


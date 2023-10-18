"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import payrollreportresponse as shared_payrollreportresponse
from typing import Optional


@dataclasses.dataclass
class ListPayablesPayrollRequest:
    payroll_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'payrollId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier of a invoice with some constraints like invoice type"""
    



@dataclasses.dataclass
class ListPayablesPayrollResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    payroll_report_response: Optional[shared_payrollreportresponse.PayrollReportResponse] = dataclasses.field(default=None)
    r"""Payroll report with line items and payroll summary"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    


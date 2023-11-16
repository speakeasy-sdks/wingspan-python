"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import paymenteligibility as shared_paymenteligibility
from typing import Optional


@dataclasses.dataclass
class GetPaymentEligibilityRequirementRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique identifier"""
    



@dataclasses.dataclass
class GetPaymentEligibilityRequirementResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    payment_eligibility: Optional[shared_paymenteligibility.PaymentEligibility] = dataclasses.field(default=None)
    r"""See payment eligibility requirements on member"""
    


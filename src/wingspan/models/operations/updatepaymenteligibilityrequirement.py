"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import paymenteligibility as shared_paymenteligibility
from ..shared import paymenteligibilityupdaterequest as shared_paymenteligibilityupdaterequest
from typing import Optional



@dataclasses.dataclass
class UpdatePaymentEligibilityRequirementRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique identifier"""
    payment_eligibility_update_request: Optional[shared_paymenteligibilityupdaterequest.PaymentEligibilityUpdateRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    




@dataclasses.dataclass
class UpdatePaymentEligibilityRequirementResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    payment_eligibility: Optional[shared_paymenteligibility.PaymentEligibility] = dataclasses.field(default=None)
    r"""See payment eligibility requirements on member"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

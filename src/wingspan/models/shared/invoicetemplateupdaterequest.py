"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .frequencyupdate import FrequencyUpdate
from .invoiceupdaterequest import InvoiceUpdateRequest
from .scheduledateupdate import ScheduleDateUpdate
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Dict, List, Optional
from wingspan import utils

class StatusInvoiceTemplateUpdateRequest(str, Enum):
    ACTIVE = 'Active'
    DRAFT = 'Draft'
    EXPIRED = 'Expired'
    CANCELLED = 'Cancelled'
    LESS_THAN_NIL_GREATER_THAN_ = '<nil>'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class InvoiceTemplateUpdateRequest:
    UNSET='__SPEAKEASY_UNSET__'
    account_id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountId'), 'exclude': lambda f: f is InvoiceTemplateUpdateRequest.UNSET }})
    auto_payment_required: Optional[bool] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('autoPaymentRequired'), 'exclude': lambda f: f is InvoiceTemplateUpdateRequest.UNSET }})
    due_in_days: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dueInDays'), 'exclude': lambda f: f is InvoiceTemplateUpdateRequest.UNSET }})
    frequency: Optional[FrequencyUpdate] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('frequency'), 'exclude': lambda f: f is InvoiceTemplateUpdateRequest.UNSET }})
    invoice_data: Optional[InvoiceUpdateRequest] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceData'), 'exclude': lambda f: f is InvoiceTemplateUpdateRequest.UNSET }})
    is_scheduling_only: Optional[bool] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isSchedulingOnly'), 'exclude': lambda f: f is InvoiceTemplateUpdateRequest.UNSET }})
    labels: Optional[Dict[str, str]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels'), 'exclude': lambda f: f is InvoiceTemplateUpdateRequest.UNSET }})
    payment_method_id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paymentMethodId'), 'exclude': lambda f: f is InvoiceTemplateUpdateRequest.UNSET }})
    schedule_dates: Optional[List[ScheduleDateUpdate]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scheduleDates'), 'exclude': lambda f: f is InvoiceTemplateUpdateRequest.UNSET }})
    send_emails: Optional[bool] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sendEmails'), 'exclude': lambda f: f is InvoiceTemplateUpdateRequest.UNSET }})
    status: Optional[StatusInvoiceTemplateUpdateRequest] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is InvoiceTemplateUpdateRequest.UNSET }})
    


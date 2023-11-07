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
    account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountId') }})
    auto_payment_required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('autoPaymentRequired') }})
    due_in_days: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dueInDays') }})
    frequency: Optional[FrequencyUpdate] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('frequency') }})
    invoice_data: Optional[InvoiceUpdateRequest] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceData') }})
    is_scheduling_only: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isSchedulingOnly') }})
    labels: Optional[Dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels') }})
    payment_method_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paymentMethodId') }})
    schedule_dates: Optional[List[ScheduleDateUpdate]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scheduleDates') }})
    send_emails: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sendEmails') }})
    status: Optional[StatusInvoiceTemplateUpdateRequest] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    


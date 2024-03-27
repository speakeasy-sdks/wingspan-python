"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .frequency import Frequency
from .invoice import Invoice
from .scheduledate import ScheduleDate
from .userroles import UserRoles
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Dict, List, Optional
from wingspan import utils

class StatusInvoiceTemplate(str, Enum):
    ACTIVE = 'Active'
    DRAFT = 'Draft'
    EXPIRED = 'Expired'
    CANCELLED = 'Cancelled'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class InvoiceTemplate:
    UNSET='__SPEAKEASY_UNSET__'
    created_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt') }})
    invoice_data: Invoice = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceData') }})
    invoice_template_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceTemplateId') }})
    labels: Dict[str, str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels') }})
    member_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberId') }})
    status: StatusInvoiceTemplate = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    updated_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt') }})
    user_roles: UserRoles = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userRoles') }})
    account_id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountId'), 'exclude': lambda f: f is InvoiceTemplate.UNSET }})
    auto_payment_required: Optional[bool] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('autoPaymentRequired'), 'exclude': lambda f: f is InvoiceTemplate.UNSET }})
    created_invoice_id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdInvoiceId'), 'exclude': lambda f: f is InvoiceTemplate.UNSET }})
    due_in_days: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dueInDays'), 'exclude': lambda f: f is InvoiceTemplate.UNSET }})
    frequency: Optional[Frequency] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('frequency'), 'exclude': lambda f: f is InvoiceTemplate.UNSET }})
    is_scheduling_only: Optional[bool] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isSchedulingOnly'), 'exclude': lambda f: f is InvoiceTemplate.UNSET }})
    last_invoice_date: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lastInvoiceDate'), 'exclude': lambda f: f is InvoiceTemplate.UNSET }})
    next_invoice_date: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nextInvoiceDate'), 'exclude': lambda f: f is InvoiceTemplate.UNSET }})
    payment_method_id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paymentMethodId'), 'exclude': lambda f: f is InvoiceTemplate.UNSET }})
    schedule_dates: Optional[List[ScheduleDate]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scheduleDates'), 'exclude': lambda f: f is InvoiceTemplate.UNSET }})
    


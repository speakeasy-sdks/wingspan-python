"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import clientinvoice as shared_clientinvoice
from ..shared import frequency as shared_frequency
from ..shared import scheduledate as shared_scheduledate
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import List, Optional
from wingspan import utils

class StatusClientInvoiceTemplate(str, Enum):
    ACTIVE = 'Active'
    DRAFT = 'Draft'
    EXPIRED = 'Expired'
    CANCELLED = 'Cancelled'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ClientInvoiceTemplate:
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientId') }})
    created_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt') }})
    invoice_data: shared_clientinvoice.ClientInvoice = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceData') }})
    invoice_template_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceTemplateId') }})
    member_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberId') }})
    next_invoice_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nextInvoiceDate') }})
    schedule_dates: List[shared_scheduledate.ScheduleDate] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scheduleDates') }})
    status: StatusClientInvoiceTemplate = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    updated_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt') }})
    account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountId') }})
    created_invoice_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdInvoiceId') }})
    due_in_days: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dueInDays') }})
    frequency: Optional[shared_frequency.Frequency] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('frequency') }})
    payment_method_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paymentMethodId') }})
    


"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional
from wingspan import utils

class Status42f004011439ceedfeb392c84d36ad40443a5a0446d1efa02369c56e930a1c07(str, Enum):
    DRAFT = 'Draft'
    OPEN = 'Open'
    OVERDUE = 'Overdue'
    CANCELLED = 'Cancelled'
    PENDING = 'Pending'
    PAYMENT_IN_TRANSIT = 'PaymentInTransit'
    PAID = 'Paid'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class FortyTwof004011439ceedfeb392c84d36ad40443a5a0446d1efa02369c56e930a1c07:
    created_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt') }})
    due_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dueDate') }})
    invoice_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceId') }})
    invoice_number: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceNumber') }})
    status: Status42f004011439ceedfeb392c84d36ad40443a5a0446d1efa02369c56e930a1c07 = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    updated_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt') }})
    deposited_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('depositedDate') }})
    notes: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('notes') }})
    paid_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paidDate') }})
    


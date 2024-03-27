"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from wingspan import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PayablesSummary:
    invoices_approved: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoicesApproved') }})
    invoices_draft: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoicesDraft') }})
    invoices_open: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoicesOpen') }})
    invoices_overdue: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoicesOverdue') }})
    invoices_paid: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoicesPaid') }})
    invoices_pending: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoicesPending') }})
    member_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberId') }})
    total_approved: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalApproved') }})
    total_open: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalOpen') }})
    total_overdue: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalOverdue') }})
    total_paid: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalPaid') }})
    


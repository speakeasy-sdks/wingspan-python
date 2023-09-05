"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional
from wingspan import utils

class InvoiceUpdateRequestAcceptedPaymentMethods(str, Enum):
    CREDIT = 'Credit'
    ACH = 'ACH'
    MANUAL = 'Manual'
    LESS_THAN_NIL_GREATER_THAN_ = '<nil>'



@dataclasses.dataclass
class InvoiceUpdateRequestClient2:
    pass



@dataclasses.dataclass
class InvoiceUpdateRequestMember2:
    pass

class StatusInvoiceUpdateRequest(str, Enum):
    DRAFT = 'Draft'
    OPEN = 'Open'
    OVERDUE = 'Overdue'
    CANCELLED = 'Cancelled'
    PENDING = 'Pending'
    PAYMENT_IN_TRANSIT = 'PaymentInTransit'
    PAID = 'Paid'
    LESS_THAN_NIL_GREATER_THAN_ = '<nil>'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class InvoiceUpdateRequest:
    accepted_payment_methods: Optional[list[InvoiceUpdateRequestAcceptedPaymentMethods]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('acceptedPaymentMethods'), 'exclude': lambda f: f is None }})
    attachments: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attachments'), 'exclude': lambda f: f is None }})
    charged_fees: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('chargedFees'), 'exclude': lambda f: f is None }})
    client: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client'), 'exclude': lambda f: f is None }})
    collaborators: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collaborators'), 'exclude': lambda f: f is None }})
    credit_fee_handling: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('creditFeeHandling'), 'exclude': lambda f: f is None }})
    due_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dueDate'), 'exclude': lambda f: f is None }})
    integration: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('integration'), 'exclude': lambda f: f is None }})
    invoice_notes: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceNotes'), 'exclude': lambda f: f is None }})
    labels: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels'), 'exclude': lambda f: f is None }})
    late_fee_handling: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lateFeeHandling'), 'exclude': lambda f: f is None }})
    line_items: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lineItems'), 'exclude': lambda f: f is None }})
    member: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('member'), 'exclude': lambda f: f is None }})
    member_client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberClientId'), 'exclude': lambda f: f is None }})
    metadata: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    notification_preferences: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('notificationPreferences'), 'exclude': lambda f: f is None }})
    status: Optional[StatusInvoiceUpdateRequest] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    

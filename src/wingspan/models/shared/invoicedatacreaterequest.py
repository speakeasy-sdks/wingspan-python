"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import invoicelineitemscreaterequest as shared_invoicelineitemscreaterequest
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional
from wingspan import utils

class InvoiceDataCreateRequestAcceptedPaymentMethods(str, Enum):
    CREDIT = 'Credit'
    ACH = 'ACH'
    MANUAL = 'Manual'
    LESS_THAN_NIL_GREATER_THAN_ = '<nil>'

class CurrencyInvoiceDataCreateRequest(str, Enum):
    USD = 'USD'
    CAD = 'CAD'
    LESS_THAN_NIL_GREATER_THAN_ = '<nil>'

class StatusInvoiceDataCreateRequest(str, Enum):
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
class InvoiceDataCreateRequest:
    line_items: list[shared_invoicelineitemscreaterequest.InvoiceLineItemsCreateRequest] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lineItems') }})
    member_client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberClientId') }})
    accepted_payment_methods: Optional[list[InvoiceDataCreateRequestAcceptedPaymentMethods]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('acceptedPaymentMethods'), 'exclude': lambda f: f is None }})
    attachments: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attachments'), 'exclude': lambda f: f is None }})
    collaborators: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collaborators'), 'exclude': lambda f: f is None }})
    credit_fee_handling: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('creditFeeHandling'), 'exclude': lambda f: f is None }})
    currency: Optional[CurrencyInvoiceDataCreateRequest] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency'), 'exclude': lambda f: f is None }})
    due_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dueDate'), 'exclude': lambda f: f is None }})
    invoice_notes: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceNotes'), 'exclude': lambda f: f is None }})
    labels: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels'), 'exclude': lambda f: f is None }})
    late_fee_handling: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lateFeeHandling'), 'exclude': lambda f: f is None }})
    notification_preferences: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('notificationPreferences'), 'exclude': lambda f: f is None }})
    status: Optional[StatusInvoiceDataCreateRequest] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    


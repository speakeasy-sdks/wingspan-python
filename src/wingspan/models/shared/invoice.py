"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import address as shared_address
from ..shared import clientoptions as shared_clientoptions
from ..shared import externalids as shared_externalids
from ..shared import invoiceevents as shared_invoiceevents
from ..shared import invoicelineitem as shared_invoicelineitem
from ..shared import memberoptions as shared_memberoptions
from ..shared import userroles as shared_userroles
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional
from wingspan import utils

class InvoiceAcceptedPaymentMethods(str, Enum):
    CREDIT = 'Credit'
    ACH = 'ACH'
    MANUAL = 'Manual'
    LESS_THAN_NIL_GREATER_THAN_ = '<nil>'

class CurrencyInvoice(str, Enum):
    USD = 'USD'
    CAD = 'CAD'

class StatusInvoice(str, Enum):
    DRAFT = 'Draft'
    OPEN = 'Open'
    OVERDUE = 'Overdue'
    CANCELLED = 'Cancelled'
    PENDING = 'Pending'
    PAYMENT_IN_TRANSIT = 'PaymentInTransit'
    PAID = 'Paid'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class Invoice:
    r"""An invoice"""
    amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount') }})
    client: shared_clientoptions.ClientOptions = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client') }})
    created_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt') }})
    currency: CurrencyInvoice = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency') }})
    due_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dueDate') }})
    events: shared_invoiceevents.InvoiceEvents = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('events') }})
    external_ids: shared_externalids.ExternalIds = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('externalIds') }})
    invoice_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceId') }})
    invoice_number: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceNumber') }})
    labels: dict[str, str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels') }})
    line_items: list[shared_invoicelineitem.InvoiceLineItem] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lineItems') }})
    member: shared_memberoptions.MemberOptions = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('member') }})
    member_address: shared_address.Address = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberAddress') }})
    member_client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberClientId') }})
    member_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberId') }})
    status: StatusInvoice = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    updated_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt') }})
    user_roles: shared_userroles.UserRoles = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userRoles') }})
    accepted_payment_methods: Optional[list[InvoiceAcceptedPaymentMethods]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('acceptedPaymentMethods'), 'exclude': lambda f: f is None }})
    account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountId'), 'exclude': lambda f: f is None }})
    amount_details: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amountDetails'), 'exclude': lambda f: f is None }})
    attachments: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attachments'), 'exclude': lambda f: f is None }})
    bank_transfer_info: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bankTransferInfo'), 'exclude': lambda f: f is None }})
    charged_fees: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('chargedFees'), 'exclude': lambda f: f is None }})
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientId'), 'exclude': lambda f: f is None }})
    collaborators: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collaborators'), 'exclude': lambda f: f is None }})
    credit_fee_handling: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('creditFeeHandling'), 'exclude': lambda f: f is None }})
    deductions: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deductions'), 'exclude': lambda f: f is None }})
    integration: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('integration'), 'exclude': lambda f: f is None }})
    international_bank_transfer_info: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('internationalBankTransferInfo'), 'exclude': lambda f: f is None }})
    invoice_notes: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceNotes'), 'exclude': lambda f: f is None }})
    invoice_template_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceTemplateId'), 'exclude': lambda f: f is None }})
    late_fee_handling: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lateFeeHandling'), 'exclude': lambda f: f is None }})
    member_formatted_address_lines: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberFormattedAddressLines'), 'exclude': lambda f: f is None }})
    metadata: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    notification_preferences: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('notificationPreferences'), 'exclude': lambda f: f is None }})
    parent_invoice_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parentInvoiceId'), 'exclude': lambda f: f is None }})
    payment_info: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paymentInfo'), 'exclude': lambda f: f is None }})
    payment_method_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paymentMethodId'), 'exclude': lambda f: f is None }})
    payout_destinations: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payoutDestinations'), 'exclude': lambda f: f is None }})
    processing_fees: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('processingFees'), 'exclude': lambda f: f is None }})
    source_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceId'), 'exclude': lambda f: f is None }})
    withholdings: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('withholdings'), 'exclude': lambda f: f is None }})
    


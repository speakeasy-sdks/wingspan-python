"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import address as shared_address
from ..shared import clientoptions as shared_clientoptions
from ..shared import invoiceevents as shared_invoiceevents
from ..shared import invoicelineitem as shared_invoicelineitem
from ..shared import memberclient as shared_memberclient
from ..shared import memberoptions as shared_memberoptions
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional
from wingspan import utils

class ClientInvoiceAcceptedPaymentMethods(str, Enum):
    CREDIT = 'Credit'
    ACH = 'ACH'
    MANUAL = 'Manual'
    LESS_THAN_NIL_GREATER_THAN_ = '<nil>'

class ClientInvoiceCurrency(str, Enum):
    USD = 'USD'
    CAD = 'CAD'

class StatusClientInvoice(str, Enum):
    DRAFT = 'Draft'
    OPEN = 'Open'
    OVERDUE = 'Overdue'
    CANCELLED = 'Cancelled'
    PENDING = 'Pending'
    PAYMENT_IN_TRANSIT = 'PaymentInTransit'
    PAID = 'Paid'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ClientInvoice:
    r"""A client created invoice"""
    additional_recipient_emails: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('additionalRecipientEmails') }})
    amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount') }})
    client: shared_clientoptions.ClientOptions = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client') }})
    created_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt') }})
    currency: ClientInvoiceCurrency = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency') }})
    due_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dueDate') }})
    events: shared_invoiceevents.InvoiceEvents = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('events') }})
    invoice_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceId') }})
    invoice_number: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceNumber') }})
    line_items: list[shared_invoicelineitem.InvoiceLineItem] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lineItems') }})
    member: shared_memberoptions.MemberOptions = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('member') }})
    member_accepts_payments: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberAcceptsPayments') }})
    member_address: shared_address.Address = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberAddress') }})
    member_client: shared_memberclient.MemberClient = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberClient') }})
    member_company: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberCompany') }})
    member_email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberEmail') }})
    member_logo_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberLogoUrl') }})
    member_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberName') }})
    member_payments_version: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberPaymentsVersion') }})
    member_stripe_account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberStripeAccountId') }})
    project_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('projectName') }})
    status: StatusClientInvoice = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    updated_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt') }})
    accepted_payment_methods: Optional[list[ClientInvoiceAcceptedPaymentMethods]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('acceptedPaymentMethods'), 'exclude': lambda f: f is None }})
    account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountId'), 'exclude': lambda f: f is None }})
    attachments: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attachments'), 'exclude': lambda f: f is None }})
    bank_transfer_info: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bankTransferInfo'), 'exclude': lambda f: f is None }})
    charged_fees: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('chargedFees'), 'exclude': lambda f: f is None }})
    credit_fee_handling: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('creditFeeHandling'), 'exclude': lambda f: f is None }})
    integration: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('integration'), 'exclude': lambda f: f is None }})
    international_bank_transfer_info: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('internationalBankTransferInfo'), 'exclude': lambda f: f is None }})
    invoice_notes: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceNotes'), 'exclude': lambda f: f is None }})
    invoice_template_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceTemplateId'), 'exclude': lambda f: f is None }})
    late_fee_handling: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lateFeeHandling'), 'exclude': lambda f: f is None }})
    member_formatted_address_lines: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberFormattedAddressLines'), 'exclude': lambda f: f is None }})
    metadata: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    payment_info: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paymentInfo'), 'exclude': lambda f: f is None }})
    payment_method_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paymentMethodId'), 'exclude': lambda f: f is None }})
    processing_fees: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('processingFees'), 'exclude': lambda f: f is None }})
    source_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceId'), 'exclude': lambda f: f is None }})
    

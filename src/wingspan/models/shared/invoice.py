"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .address import Address
from .bankaccount import BankAccount
from .clientoptions import ClientOptions
from .externalids import ExternalIds
from .feehandlingconfig import FeeHandlingConfig
from .fees import Fees
from .invoiceamountdetails import InvoiceAmountDetails
from .invoiceapplieddeductions import InvoiceAppliedDeductions
from .invoiceattachments import InvoiceAttachments
from .invoicecollaborator import InvoiceCollaborator
from .invoiceevents import InvoiceEvents
from .invoiceintegrations import InvoiceIntegrations
from .invoicelineitem import InvoiceLineItem
from .invoicemetadata import InvoiceMetadata
from .invoicenotificationpreferences import InvoiceNotificationPreferences
from .invoicepayoutdestination import InvoicePayoutDestination
from .invoicewithholdings import InvoiceWithholdings
from .latefeeconfig import LateFeeConfig
from .memberoptions import MemberOptions
from .paymentinfo import PaymentInfo
from .processingfees import ProcessingFees
from .userroles import UserRoles
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Dict, List, Optional
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
    amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount') }})
    client: ClientOptions = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client') }})
    created_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt') }})
    currency: CurrencyInvoice = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency') }})
    due_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dueDate') }})
    events: InvoiceEvents = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('events') }})
    external_ids: ExternalIds = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('externalIds') }})
    invoice_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceId') }})
    invoice_number: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceNumber') }})
    labels: Dict[str, str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels') }})
    line_items: List[InvoiceLineItem] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lineItems') }})
    member: MemberOptions = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('member') }})
    member_address: Address = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberAddress') }})
    member_client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberClientId') }})
    member_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberId') }})
    status: StatusInvoice = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    updated_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt') }})
    user_roles: UserRoles = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userRoles') }})
    accepted_payment_methods: Optional[List[InvoiceAcceptedPaymentMethods]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('acceptedPaymentMethods') }})
    account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountId') }})
    amount_details: Optional[InvoiceAmountDetails] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amountDetails') }})
    attachments: Optional[InvoiceAttachments] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attachments') }})
    bank_transfer_info: Optional[BankAccount] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bankTransferInfo') }})
    charged_fees: Optional[Fees] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('chargedFees') }})
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientId') }})
    collaborators: Optional[List[InvoiceCollaborator]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collaborators') }})
    credit_fee_handling: Optional[FeeHandlingConfig] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('creditFeeHandling') }})
    deductions: Optional[List[InvoiceAppliedDeductions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deductions') }})
    integration: Optional[InvoiceIntegrations] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('integration') }})
    international_bank_transfer_info: Optional[BankAccount] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('internationalBankTransferInfo') }})
    invoice_notes: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceNotes') }})
    invoice_template_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceTemplateId') }})
    late_fee_handling: Optional[LateFeeConfig] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lateFeeHandling') }})
    member_formatted_address_lines: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberFormattedAddressLines') }})
    metadata: Optional[InvoiceMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata') }})
    notification_preferences: Optional[InvoiceNotificationPreferences] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('notificationPreferences') }})
    parent_invoice_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parentInvoiceId') }})
    payment_info: Optional[PaymentInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paymentInfo') }})
    payment_method_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paymentMethodId') }})
    payout_destinations: Optional[List[InvoicePayoutDestination]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payoutDestinations') }})
    processing_fees: Optional[ProcessingFees] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('processingFees') }})
    source_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceId') }})
    withholdings: Optional[InvoiceWithholdings] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('withholdings') }})
    


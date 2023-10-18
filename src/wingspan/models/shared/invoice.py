"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import address as shared_address
from ..shared import bankaccount as shared_bankaccount
from ..shared import clientoptions as shared_clientoptions
from ..shared import externalids as shared_externalids
from ..shared import feehandlingconfig as shared_feehandlingconfig
from ..shared import fees as shared_fees
from ..shared import invoiceamountdetails as shared_invoiceamountdetails
from ..shared import invoiceapplieddeductions as shared_invoiceapplieddeductions
from ..shared import invoiceattachments as shared_invoiceattachments
from ..shared import invoicecollaborator as shared_invoicecollaborator
from ..shared import invoiceevents as shared_invoiceevents
from ..shared import invoiceintegrations as shared_invoiceintegrations
from ..shared import invoicelineitem as shared_invoicelineitem
from ..shared import invoicemetadata as shared_invoicemetadata
from ..shared import invoicenotificationpreferences as shared_invoicenotificationpreferences
from ..shared import invoicepayoutdestination as shared_invoicepayoutdestination
from ..shared import invoicewithholdings as shared_invoicewithholdings
from ..shared import latefeeconfig as shared_latefeeconfig
from ..shared import memberoptions as shared_memberoptions
from ..shared import paymentinfo as shared_paymentinfo
from ..shared import processingfees as shared_processingfees
from ..shared import userroles as shared_userroles
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
    client: shared_clientoptions.ClientOptions = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client') }})
    created_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt') }})
    currency: CurrencyInvoice = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency') }})
    due_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dueDate') }})
    events: shared_invoiceevents.InvoiceEvents = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('events') }})
    external_ids: shared_externalids.ExternalIds = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('externalIds') }})
    invoice_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceId') }})
    invoice_number: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceNumber') }})
    labels: Dict[str, str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels') }})
    line_items: List[shared_invoicelineitem.InvoiceLineItem] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lineItems') }})
    member: shared_memberoptions.MemberOptions = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('member') }})
    member_address: shared_address.Address = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberAddress') }})
    member_client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberClientId') }})
    member_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberId') }})
    status: StatusInvoice = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    updated_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt') }})
    user_roles: shared_userroles.UserRoles = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userRoles') }})
    accepted_payment_methods: Optional[List[InvoiceAcceptedPaymentMethods]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('acceptedPaymentMethods') }})
    account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountId') }})
    amount_details: Optional[shared_invoiceamountdetails.InvoiceAmountDetails] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amountDetails') }})
    attachments: Optional[shared_invoiceattachments.InvoiceAttachments] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attachments') }})
    bank_transfer_info: Optional[shared_bankaccount.BankAccount] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bankTransferInfo') }})
    charged_fees: Optional[shared_fees.Fees] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('chargedFees') }})
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientId') }})
    collaborators: Optional[List[shared_invoicecollaborator.InvoiceCollaborator]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collaborators') }})
    credit_fee_handling: Optional[shared_feehandlingconfig.FeeHandlingConfig] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('creditFeeHandling') }})
    deductions: Optional[List[shared_invoiceapplieddeductions.InvoiceAppliedDeductions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deductions') }})
    integration: Optional[shared_invoiceintegrations.InvoiceIntegrations] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('integration') }})
    international_bank_transfer_info: Optional[shared_bankaccount.BankAccount] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('internationalBankTransferInfo') }})
    invoice_notes: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceNotes') }})
    invoice_template_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceTemplateId') }})
    late_fee_handling: Optional[shared_latefeeconfig.LateFeeConfig] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lateFeeHandling') }})
    member_formatted_address_lines: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberFormattedAddressLines') }})
    metadata: Optional[shared_invoicemetadata.InvoiceMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata') }})
    notification_preferences: Optional[shared_invoicenotificationpreferences.InvoiceNotificationPreferences] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('notificationPreferences') }})
    parent_invoice_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parentInvoiceId') }})
    payment_info: Optional[shared_paymentinfo.PaymentInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paymentInfo') }})
    payment_method_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paymentMethodId') }})
    payout_destinations: Optional[List[shared_invoicepayoutdestination.InvoicePayoutDestination]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payoutDestinations') }})
    processing_fees: Optional[shared_processingfees.ProcessingFees] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('processingFees') }})
    source_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceId') }})
    withholdings: Optional[shared_invoicewithholdings.InvoiceWithholdings] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('withholdings') }})
    


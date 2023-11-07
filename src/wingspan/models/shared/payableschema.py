"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .address import Address
from .bankaccount import BankAccount
from .clientoptions import ClientOptions
from .feehandlingconfig import FeeHandlingConfig
from .fees import Fees
from .invoiceattachments import InvoiceAttachments
from .invoiceevents import InvoiceEvents
from .invoicelineitem import InvoiceLineItem
from .invoicemetadata import InvoiceMetadata
from .invoicenotificationpreferences import InvoiceNotificationPreferences
from .latefeeconfig import LateFeeConfig
from .memberoptions import MemberOptions
from .scheduledate import ScheduleDate
from .sixb94b58d661f3eabc1444a7a43ac4b99580f0d050123b7bf38184e2f0d7bd66e import Sixb94b58d661f3eabc1444a7a43ac4b99580f0d050123b7bf38184e2f0d7bd66e
from .userroles import UserRoles
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Dict, List, Optional
from wingspan import utils

class PayableSchemaAcceptedPaymentMethods(str, Enum):
    CREDIT = 'Credit'
    ACH = 'ACH'
    MANUAL = 'Manual'
    LESS_THAN_NIL_GREATER_THAN_ = '<nil>'

class CurrencyPayableSchema(str, Enum):
    USD = 'USD'
    CAD = 'CAD'

class StatusPayableSchema(str, Enum):
    DRAFT = 'Draft'
    OPEN = 'Open'
    OVERDUE = 'Overdue'
    CANCELLED = 'Cancelled'
    PENDING = 'Pending'
    PAYMENT_IN_TRANSIT = 'PaymentInTransit'
    PAID = 'Paid'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PayableSchema:
    amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount') }})
    attachments: InvoiceAttachments = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attachments') }})
    client: ClientOptions = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client') }})
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientId') }})
    collaborator_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collaboratorId') }})
    created_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt') }})
    credit_fee_handling: FeeHandlingConfig = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('creditFeeHandling') }})
    currency: CurrencyPayableSchema = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency') }})
    due_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dueDate') }})
    events: InvoiceEvents = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('events') }})
    integration: Sixb94b58d661f3eabc1444a7a43ac4b99580f0d050123b7bf38184e2f0d7bd66e = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('integration') }})
    invoice_notes: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceNotes') }})
    invoice_number: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceNumber') }})
    invoice_template_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceTemplateId') }})
    labels: Dict[str, str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels') }})
    late_fee_handling: LateFeeConfig = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lateFeeHandling') }})
    line_items: List[InvoiceLineItem] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lineItems') }})
    member: MemberOptions = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('member') }})
    member_address: Address = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberAddress') }})
    member_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberId') }})
    notification_preferences: InvoiceNotificationPreferences = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('notificationPreferences') }})
    payable_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payableId') }})
    status: StatusPayableSchema = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    updated_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt') }})
    user_roles: UserRoles = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userRoles') }})
    accepted_payment_methods: Optional[List[PayableSchemaAcceptedPaymentMethods]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('acceptedPaymentMethods') }})
    account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountId') }})
    bank_transfer_info: Optional[BankAccount] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bankTransferInfo') }})
    charged_fees: Optional[Fees] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('chargedFees') }})
    international_bank_transfer_info: Optional[BankAccount] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('internationalBankTransferInfo') }})
    member_formatted_address_lines: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberFormattedAddressLines') }})
    metadata: Optional[InvoiceMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata') }})
    next_payroll_execution_date: Optional[ScheduleDate] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nextPayrollExecutionDate') }})
    payment_method_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paymentMethodId') }})
    source_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceId') }})
    


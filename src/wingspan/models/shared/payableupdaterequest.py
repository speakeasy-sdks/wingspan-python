"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .feehandlingconfig import FeeHandlingConfig
from .fees import Fees
from .invoicecollaboratorupdaterequest import InvoiceCollaboratorUpdateRequest
from .invoicelineitemscreaterequest import InvoiceLineItemsCreateRequest
from .invoicemetadata import InvoiceMetadata
from .invoicenotificationpreferences import InvoiceNotificationPreferences
from .latefeeconfigupdate import LateFeeConfigUpdate
from .thirty_sixb041d426951ffff76360faf03ef8ae938bed9739e6ad9f51acb982782296a2 import ThirtySixb041d426951ffff76360faf03ef8ae938bed9739e6ad9f51acb982782296a2
from .three_billion_one_hundred_and_ninety_million_six_hundred_and_eighty_five_thousand_eight_hundred_and_thirty_twoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461 import ThreeBillionOneHundredAndNinetyMillionSixHundredAndEightyFiveThousandEightHundredAndThirtyTwoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Dict, List, Optional
from wingspan import utils

class PayableUpdateRequestAcceptedPaymentMethods(str, Enum):
    CREDIT = 'Credit'
    ACH = 'ACH'
    MANUAL = 'Manual'


@dataclasses.dataclass
class PayableUpdateRequestClient:
    pass


@dataclasses.dataclass
class PayableUpdateRequestMember:
    pass

class PaymentMethods(str, Enum):
    CREDIT = 'Credit'
    ACH = 'ACH'
    MANUAL = 'Manual'

class StatusPayableUpdateRequest(str, Enum):
    DRAFT = 'Draft'
    OPEN = 'Open'
    OVERDUE = 'Overdue'
    CANCELLED = 'Cancelled'
    PENDING = 'Pending'
    PAYMENT_IN_TRANSIT = 'PaymentInTransit'
    PAID = 'Paid'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PayableUpdateRequest:
    UNSET='__SPEAKEASY_UNSET__'
    accepted_payment_methods: Optional[List[PayableUpdateRequestAcceptedPaymentMethods]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('acceptedPaymentMethods'), 'exclude': lambda f: f is PayableUpdateRequest.UNSET }})
    attachments: Optional[ThirtySixb041d426951ffff76360faf03ef8ae938bed9739e6ad9f51acb982782296a2] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attachments'), 'exclude': lambda f: f is PayableUpdateRequest.UNSET }})
    charged_fees: Optional[Fees] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('chargedFees'), 'exclude': lambda f: f is PayableUpdateRequest.UNSET }})
    client: Optional[PayableUpdateRequestClient] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client'), 'exclude': lambda f: f is PayableUpdateRequest.UNSET }})
    collaborators: Optional[List[InvoiceCollaboratorUpdateRequest]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collaborators'), 'exclude': lambda f: f is PayableUpdateRequest.UNSET }})
    credit_fee_handling: Optional[FeeHandlingConfig] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('creditFeeHandling'), 'exclude': lambda f: f is PayableUpdateRequest.UNSET }})
    due_date: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dueDate'), 'exclude': lambda f: f is PayableUpdateRequest.UNSET }})
    integration: Optional[ThreeBillionOneHundredAndNinetyMillionSixHundredAndEightyFiveThousandEightHundredAndThirtyTwoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('integration'), 'exclude': lambda f: f is PayableUpdateRequest.UNSET }})
    invoice_notes: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceNotes'), 'exclude': lambda f: f is PayableUpdateRequest.UNSET }})
    labels: Optional[Dict[str, str]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels'), 'exclude': lambda f: f is PayableUpdateRequest.UNSET }})
    late_fee_handling: Optional[LateFeeConfigUpdate] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lateFeeHandling'), 'exclude': lambda f: f is PayableUpdateRequest.UNSET }})
    line_items: Optional[List[InvoiceLineItemsCreateRequest]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lineItems'), 'exclude': lambda f: f is PayableUpdateRequest.UNSET }})
    member: Optional[PayableUpdateRequestMember] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('member'), 'exclude': lambda f: f is PayableUpdateRequest.UNSET }})
    member_client_id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberClientId'), 'exclude': lambda f: f is PayableUpdateRequest.UNSET }})
    metadata: Optional[InvoiceMetadata] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is PayableUpdateRequest.UNSET }})
    notification_preferences: Optional[InvoiceNotificationPreferences] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('notificationPreferences'), 'exclude': lambda f: f is PayableUpdateRequest.UNSET }})
    payment_methods: Optional[List[PaymentMethods]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paymentMethods'), 'exclude': lambda f: f is PayableUpdateRequest.UNSET }})
    status: Optional[StatusPayableUpdateRequest] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is PayableUpdateRequest.UNSET }})
    


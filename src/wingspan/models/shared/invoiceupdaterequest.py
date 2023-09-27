"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import feehandlingconfig as shared_feehandlingconfig
from ..shared import fees as shared_fees
from ..shared import invoicecollaboratorupdaterequest as shared_invoicecollaboratorupdaterequest
from ..shared import invoicelineitemscreaterequest as shared_invoicelineitemscreaterequest
from ..shared import invoicemetadata as shared_invoicemetadata
from ..shared import invoicenotificationpreferences as shared_invoicenotificationpreferences
from ..shared import latefeeconfigupdate as shared_latefeeconfigupdate
from ..shared import thirty_sixb041d426951ffff76360faf03ef8ae938bed9739e6ad9f51acb982782296a2 as shared_thirty_sixb041d426951ffff76360faf03ef8ae938bed9739e6ad9f51acb982782296a2
from ..shared import three_billion_one_hundred_and_ninety_million_six_hundred_and_eighty_five_thousand_eight_hundred_and_thirty_twoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461 as shared_three_billion_one_hundred_and_ninety_million_six_hundred_and_eighty_five_thousand_eight_hundred_and_thirty_twoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional, Union
from wingspan import utils

class InvoiceUpdateRequestAcceptedPaymentMethods(str, Enum):
    CREDIT = 'Credit'
    ACH = 'ACH'
    MANUAL = 'Manual'
    LESS_THAN_NIL_GREATER_THAN_ = '<nil>'



@dataclasses.dataclass
class InvoiceUpdateRequestAttachments:
    pass



@dataclasses.dataclass
class InvoiceUpdateRequestChargedFees:
    pass



@dataclasses.dataclass
class InvoiceUpdateRequestClient2:
    pass



@dataclasses.dataclass
class InvoiceUpdateRequestClient:
    pass



@dataclasses.dataclass
class InvoiceUpdateRequestCollaborators:
    pass



@dataclasses.dataclass
class InvoiceUpdateRequestCreditFeeHandling:
    pass



@dataclasses.dataclass
class InvoiceUpdateRequestIntegration:
    pass



@dataclasses.dataclass
class InvoiceUpdateRequestLabels:
    pass



@dataclasses.dataclass
class InvoiceUpdateRequestLateFeeHandling:
    pass



@dataclasses.dataclass
class InvoiceUpdateRequestLineItems:
    pass



@dataclasses.dataclass
class InvoiceUpdateRequestMember2:
    pass



@dataclasses.dataclass
class InvoiceUpdateRequestMember:
    pass



@dataclasses.dataclass
class InvoiceUpdateRequestMetadata:
    pass



@dataclasses.dataclass
class InvoiceUpdateRequestNotificationPreferences:
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
    attachments: Optional[Union[Any, shared_thirty_sixb041d426951ffff76360faf03ef8ae938bed9739e6ad9f51acb982782296a2.ThirtySixb041d426951ffff76360faf03ef8ae938bed9739e6ad9f51acb982782296a2]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attachments'), 'exclude': lambda f: f is None }})
    charged_fees: Optional[Union[Any, shared_fees.Fees]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('chargedFees'), 'exclude': lambda f: f is None }})
    client: Optional[Union[Any, InvoiceUpdateRequestClient2]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client'), 'exclude': lambda f: f is None }})
    collaborators: Optional[list[Union[Any, shared_invoicecollaboratorupdaterequest.InvoiceCollaboratorUpdateRequest]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collaborators'), 'exclude': lambda f: f is None }})
    credit_fee_handling: Optional[Union[Any, shared_feehandlingconfig.FeeHandlingConfig]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('creditFeeHandling'), 'exclude': lambda f: f is None }})
    due_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dueDate'), 'exclude': lambda f: f is None }})
    integration: Optional[Union[Any, shared_three_billion_one_hundred_and_ninety_million_six_hundred_and_eighty_five_thousand_eight_hundred_and_thirty_twoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461.ThreeBillionOneHundredAndNinetyMillionSixHundredAndEightyFiveThousandEightHundredAndThirtyTwoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('integration'), 'exclude': lambda f: f is None }})
    invoice_notes: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceNotes'), 'exclude': lambda f: f is None }})
    labels: Optional[Union[Any, dict[str, str]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels'), 'exclude': lambda f: f is None }})
    late_fee_handling: Optional[Union[Any, shared_latefeeconfigupdate.LateFeeConfigUpdate]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lateFeeHandling'), 'exclude': lambda f: f is None }})
    line_items: Optional[list[Union[Any, shared_invoicelineitemscreaterequest.InvoiceLineItemsCreateRequest]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lineItems'), 'exclude': lambda f: f is None }})
    member: Optional[Union[Any, InvoiceUpdateRequestMember2]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('member'), 'exclude': lambda f: f is None }})
    member_client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberClientId'), 'exclude': lambda f: f is None }})
    metadata: Optional[Union[Any, shared_invoicemetadata.InvoiceMetadata]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    notification_preferences: Optional[Union[Any, shared_invoicenotificationpreferences.InvoiceNotificationPreferences]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('notificationPreferences'), 'exclude': lambda f: f is None }})
    status: Optional[StatusInvoiceUpdateRequest] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    


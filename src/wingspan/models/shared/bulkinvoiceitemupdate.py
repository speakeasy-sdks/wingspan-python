"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import feehandlingconfig as shared_feehandlingconfig
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Dict, List, Optional
from wingspan import utils

class BulkInvoiceItemUpdateAcceptedPaymentMethods(str, Enum):
    CREDIT = 'Credit'
    ACH = 'ACH'
    MANUAL = 'Manual'
    LESS_THAN_NIL_GREATER_THAN_ = '<nil>'

class InvoiceStatusBulkInvoiceItemUpdate(str, Enum):
    DRAFT = 'Draft'
    OPEN = 'Open'
    APPROVED = 'Approved'
    PAID = 'Paid'
    CANCELLED = 'Cancelled'
    LESS_THAN_NIL_GREATER_THAN_ = '<nil>'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BulkInvoiceItemUpdate:
    accepted_payment_methods: Optional[List[BulkInvoiceItemUpdateAcceptedPaymentMethods]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('acceptedPaymentMethods') }})
    amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount') }})
    bulk_invoice_batch_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bulkInvoiceBatchId') }})
    bulk_invoice_item_merge_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bulkInvoiceItemMergeKey') }})
    bulk_invoice_item_reference: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bulkInvoiceItemReference') }})
    client_email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientEmail') }})
    client_external_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientExternalId') }})
    credit_fee_handling: Optional[shared_feehandlingconfig.FeeHandlingConfig] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('creditFeeHandling') }})
    due_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dueDate') }})
    invoice_notes: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceNotes') }})
    invoice_status: Optional[InvoiceStatusBulkInvoiceItemUpdate] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceStatus') }})
    labels: Optional[Dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels') }})
    line_item_description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lineItemDescription') }})
    line_item_detail: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lineItemDetail') }})
    member_client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberClientId') }})
    paid_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paidDate') }})
    project_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('projectName') }})
    reimbursable_expense: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reimbursableExpense') }})
    send_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sendDate') }})
    


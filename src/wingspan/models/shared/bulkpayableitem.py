"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import userroles as shared_userroles
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional
from wingspan import utils

class PayableStatusBulkPayableItem(str, Enum):
    DRAFT = 'Draft'
    OPEN = 'Open'
    APPROVED = 'Approved'
    PAID = 'Paid'
    CANCELLED = 'Cancelled'

class StatusBulkPayableItem(str, Enum):
    OPEN = 'Open'
    PENDING = 'Pending'
    PROCESSING = 'Processing'
    COMPLETE = 'Complete'
    FAILED = 'Failed'

class BulkPayableItemWorkflowSubStatus(str, Enum):
    SUBMITTED = 'Submitted'
    LESS_THAN_NIL_GREATER_THAN_ = '<nil>'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class BulkPayableItem:
    amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount') }})
    bulk_payable_batch_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bulkPayableBatchId') }})
    bulk_payable_item_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bulkPayableItemId') }})
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientId') }})
    created_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt') }})
    due_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dueDate') }})
    labels: dict[str, str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels') }})
    line_item_description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lineItemDescription') }})
    paid_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paidDate') }})
    payable_status: PayableStatusBulkPayableItem = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payableStatus') }})
    status: StatusBulkPayableItem = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    updated_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt') }})
    user_roles: shared_userroles.UserRoles = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userRoles') }})
    attachment_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attachmentId'), 'exclude': lambda f: f is None }})
    bulk_payable_item_merge_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bulkPayableItemMergeKey'), 'exclude': lambda f: f is None }})
    bulk_payable_item_reference: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bulkPayableItemReference'), 'exclude': lambda f: f is None }})
    collaborator_email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collaboratorEmail'), 'exclude': lambda f: f is None }})
    collaborator_external_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collaboratorExternalId'), 'exclude': lambda f: f is None }})
    collaborator_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collaboratorId'), 'exclude': lambda f: f is None }})
    integration: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('integration'), 'exclude': lambda f: f is None }})
    line_item_detail: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lineItemDetail'), 'exclude': lambda f: f is None }})
    metadata: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    payable_notes: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payableNotes'), 'exclude': lambda f: f is None }})
    reimbursable_expense: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reimbursableExpense'), 'exclude': lambda f: f is None }})
    workflow_sub_status: Optional[BulkPayableItemWorkflowSubStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workflowSubStatus'), 'exclude': lambda f: f is None }})
    


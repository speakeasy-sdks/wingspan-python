"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .seven_hundred_and_fifty_sevenf4961b94334fd41cedc27262be7b14583377703cda6490b996969bd4e66c2 import SevenHundredAndFiftySevenf4961b94334fd41cedc27262be7b14583377703cda6490b996969bd4e66c2
from .userroles import UserRoles
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Dict, Optional
from wingspan import utils

class ProcessingStrategy(str, Enum):
    MERGE = 'Merge'
    SINGLE = 'Single'

class StatusBulkInvoiceBatch(str, Enum):
    OPEN = 'Open'
    PENDING = 'Pending'
    PROCESSING = 'Processing'
    COMPLETE = 'Complete'
    FAILED = 'Failed'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BulkInvoiceBatch:
    UNSET='__SPEAKEASY_UNSET__'
    bulk_invoice_batch_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bulkInvoiceBatchId') }})
    created_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt') }})
    labels: Dict[str, str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels') }})
    member_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberId') }})
    processing_strategy: ProcessingStrategy = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('processingStrategy') }})
    status: StatusBulkInvoiceBatch = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    updated_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt') }})
    user_roles: UserRoles = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userRoles') }})
    statistics: Optional[SevenHundredAndFiftySevenf4961b94334fd41cedc27262be7b14583377703cda6490b996969bd4e66c2] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('statistics'), 'exclude': lambda f: f is BulkInvoiceBatch.UNSET }})
    


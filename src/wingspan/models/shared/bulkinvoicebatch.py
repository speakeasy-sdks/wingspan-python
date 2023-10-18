"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import seven_hundred_and_fifty_sevenf4961b94334fd41cedc27262be7b14583377703cda6490b996969bd4e66c2 as shared_seven_hundred_and_fifty_sevenf4961b94334fd41cedc27262be7b14583377703cda6490b996969bd4e66c2
from ..shared import userroles as shared_userroles
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Dict, Optional
from wingspan import utils

class BulkInvoiceBatchProcessingStrategy(str, Enum):
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
    bulk_invoice_batch_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bulkInvoiceBatchId') }})
    created_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt') }})
    labels: Dict[str, str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels') }})
    member_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberId') }})
    processing_strategy: BulkInvoiceBatchProcessingStrategy = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('processingStrategy') }})
    status: StatusBulkInvoiceBatch = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    updated_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt') }})
    user_roles: shared_userroles.UserRoles = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userRoles') }})
    statistics: Optional[shared_seven_hundred_and_fifty_sevenf4961b94334fd41cedc27262be7b14583377703cda6490b996969bd4e66c2.SevenHundredAndFiftySevenf4961b94334fd41cedc27262be7b14583377703cda6490b996969bd4e66c2] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('statistics') }})
    


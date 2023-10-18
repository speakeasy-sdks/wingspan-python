"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import redactedmember as shared_redactedmember
from ..shared import seven_hundred_and_fifty_sevenf4961b94334fd41cedc27262be7b14583377703cda6490b996969bd4e66c2 as shared_seven_hundred_and_fifty_sevenf4961b94334fd41cedc27262be7b14583377703cda6490b996969bd4e66c2
from ..shared import userroles as shared_userroles
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Dict, Optional
from wingspan import utils

class BulkPayableBatchProcessingStrategy(str, Enum):
    MERGE = 'Merge'
    SINGLE = 'Single'

class StatusBulkPayableBatch(str, Enum):
    OPEN = 'Open'
    PENDING = 'Pending'
    PROCESSING = 'Processing'
    COMPLETE = 'Complete'
    FAILED = 'Failed'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BulkPayableBatch:
    bulk_payable_batch_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bulkPayableBatchId') }})
    client: shared_redactedmember.RedactedMember = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client') }})
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientId') }})
    created_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt') }})
    labels: Dict[str, str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels') }})
    processing_strategy: BulkPayableBatchProcessingStrategy = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('processingStrategy') }})
    status: StatusBulkPayableBatch = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    updated_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt') }})
    user_roles: shared_userroles.UserRoles = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userRoles') }})
    statistics: Optional[shared_seven_hundred_and_fifty_sevenf4961b94334fd41cedc27262be7b14583377703cda6490b996969bd4e66c2.SevenHundredAndFiftySevenf4961b94334fd41cedc27262be7b14583377703cda6490b996969bd4e66c2] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('statistics') }})
    


"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .eightcf19a7bc90727398c2780566a4070199559f4723ec14c01c448dc0356efffa1 import Eightcf19a7bc90727398c2780566a4070199559f4723ec14c01c448dc0356efffa1
from .memberclientformw9info import MemberClientFormW9Info
from .userroles import UserRoles
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Dict, Optional
from wingspan import utils

class CollaboratorStatusBulkCollaboratorItem(str, Enum):
    ACTIVE = 'Active'
    INACTIVE = 'Inactive'
    PENDING = 'Pending'

class StatusBulkCollaboratorItem(str, Enum):
    OPEN = 'Open'
    PENDING = 'Pending'
    PROCESSING = 'Processing'
    COMPLETE = 'Complete'
    FAILED = 'Failed'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BulkCollaboratorItem:
    bulk_collaborator_batch_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bulkCollaboratorBatchId') }})
    bulk_collaborator_item_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bulkCollaboratorItemId') }})
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientId') }})
    collaborator_status: CollaboratorStatusBulkCollaboratorItem = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collaboratorStatus') }})
    created_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt') }})
    labels: Dict[str, str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels') }})
    status: StatusBulkCollaboratorItem = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    updated_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt') }})
    user_roles: UserRoles = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userRoles') }})
    collaborator_group_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collaboratorGroupId') }})
    collaborator_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collaboratorId') }})
    company: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('company') }})
    email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email') }})
    external_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('externalId') }})
    first_last_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('firstLastName') }})
    form_w9_data: Optional[MemberClientFormW9Info] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('formW9Data') }})
    member_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberId') }})
    metadata: Optional[Eightcf19a7bc90727398c2780566a4070199559f4723ec14c01c448dc0356efffa1] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata') }})
    


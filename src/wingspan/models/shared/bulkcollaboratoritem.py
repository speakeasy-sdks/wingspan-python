"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import eightcf19a7bc90727398c2780566a4070199559f4723ec14c01c448dc0356efffa1 as shared_eightcf19a7bc90727398c2780566a4070199559f4723ec14c01c448dc0356efffa1
from ..shared import memberclientformw9info as shared_memberclientformw9info
from ..shared import userroles as shared_userroles
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional, Union
from wingspan import utils

class CollaboratorStatusBulkCollaboratorItem(str, Enum):
    ACTIVE = 'Active'
    INACTIVE = 'Inactive'
    PENDING = 'Pending'



@dataclasses.dataclass
class BulkCollaboratorItemFormW9Data:
    pass



@dataclasses.dataclass
class BulkCollaboratorItemMetadata:
    pass

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
    labels: dict[str, str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels') }})
    status: StatusBulkCollaboratorItem = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    updated_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt') }})
    user_roles: shared_userroles.UserRoles = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userRoles') }})
    collaborator_group_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collaboratorGroupId'), 'exclude': lambda f: f is None }})
    collaborator_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collaboratorId'), 'exclude': lambda f: f is None }})
    company: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('company'), 'exclude': lambda f: f is None }})
    email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email'), 'exclude': lambda f: f is None }})
    external_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('externalId'), 'exclude': lambda f: f is None }})
    first_last_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('firstLastName'), 'exclude': lambda f: f is None }})
    form_w9_data: Optional[Union[Any, shared_memberclientformw9info.MemberClientFormW9Info]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('formW9Data'), 'exclude': lambda f: f is None }})
    member_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberId'), 'exclude': lambda f: f is None }})
    metadata: Optional[Union[Any, shared_eightcf19a7bc90727398c2780566a4070199559f4723ec14c01c448dc0356efffa1.Eightcf19a7bc90727398c2780566a4070199559f4723ec14c01c448dc0356efffa1]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    


"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import memberclientformw9info as shared_memberclientformw9info
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional, Union
from wingspan import utils

class CollaboratorStatusBulkCollaboratorItemUpdate(str, Enum):
    ACTIVE = 'Active'
    INACTIVE = 'Inactive'
    PENDING = 'Pending'
    LESS_THAN_NIL_GREATER_THAN_ = '<nil>'



@dataclasses.dataclass
class BulkCollaboratorItemUpdateFormW9Data:
    pass



@dataclasses.dataclass
class BulkCollaboratorItemUpdateLabels:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class BulkCollaboratorItemUpdate:
    collaborator_group_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collaboratorGroupId') }})
    collaborator_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collaboratorId') }})
    collaborator_status: Optional[CollaboratorStatusBulkCollaboratorItemUpdate] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collaboratorStatus') }})
    company: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('company') }})
    email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email') }})
    external_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('externalId') }})
    first_last_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('firstLastName') }})
    form_w9_data: Optional[Union[Any, shared_memberclientformw9info.MemberClientFormW9Info]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('formW9Data'), 'exclude': lambda f: f is None }})
    labels: Optional[Union[Any, dict[str, str]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels'), 'exclude': lambda f: f is None }})
    


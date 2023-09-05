"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional
from wingspan import utils

class CollaboratorStatusBulkCollaboratorItemCreate(str, Enum):
    ACTIVE = 'Active'
    INACTIVE = 'Inactive'
    PENDING = 'Pending'
    LESS_THAN_NIL_GREATER_THAN_ = '<nil>'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class BulkCollaboratorItemCreate:
    collaborator_group_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collaboratorGroupId'), 'exclude': lambda f: f is None }})
    collaborator_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collaboratorId'), 'exclude': lambda f: f is None }})
    collaborator_status: Optional[CollaboratorStatusBulkCollaboratorItemCreate] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collaboratorStatus'), 'exclude': lambda f: f is None }})
    company: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('company'), 'exclude': lambda f: f is None }})
    email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email'), 'exclude': lambda f: f is None }})
    external_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('externalId'), 'exclude': lambda f: f is None }})
    first_last_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('firstLastName'), 'exclude': lambda f: f is None }})
    form_w9_data: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('formW9Data'), 'exclude': lambda f: f is None }})
    labels: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels'), 'exclude': lambda f: f is None }})
    

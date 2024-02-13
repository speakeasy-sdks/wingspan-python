"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .d750b2d9403b5bcbdb3c96c89f1cc713df563d587f16e5f39f5ab546c08a20a0 import D750b2d9403b5bcbdb3c96c89f1cc713df563d587f16e5f39f5ab546c08a20a0
from .memberdata import MemberData
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Dict, Optional
from wingspan import utils

class ClientStatusBulkClientItemCreate(str, Enum):
    ACTIVE = 'Active'
    INACTIVE = 'Inactive'
    PENDING = 'Pending'
    LESS_THAN_NIL_GREATER_THAN_ = '<nil>'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BulkClientItemCreate:
    UNSET='__SPEAKEASY_UNSET__'
    client_status: Optional[ClientStatusBulkClientItemCreate] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientStatus'), 'exclude': lambda f: f is BulkClientItemCreate.UNSET }})
    company: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('company'), 'exclude': lambda f: f is BulkClientItemCreate.UNSET }})
    email: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email'), 'exclude': lambda f: f is BulkClientItemCreate.UNSET }})
    external_id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('externalId'), 'exclude': lambda f: f is BulkClientItemCreate.UNSET }})
    first_last_name: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('firstLastName'), 'exclude': lambda f: f is BulkClientItemCreate.UNSET }})
    integration: Optional[D750b2d9403b5bcbdb3c96c89f1cc713df563d587f16e5f39f5ab546c08a20a0] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('integration'), 'exclude': lambda f: f is BulkClientItemCreate.UNSET }})
    labels: Optional[Dict[str, str]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels'), 'exclude': lambda f: f is BulkClientItemCreate.UNSET }})
    member_data: Optional[MemberData] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberData'), 'exclude': lambda f: f is BulkClientItemCreate.UNSET }})
    


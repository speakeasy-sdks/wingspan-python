"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from petstore import utils

class CardUpdateRequestStatus(str, Enum):
    ACTIVE = 'Active'
    INACTIVE = 'Inactive'
    STOLEN = 'Stolen'
    LOST = 'Lost'
    FROZEN = 'Frozen'
    CLOSED_BY_CUSTOMER = 'ClosedByCustomer'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CardUpdateRequest:
    status: CardUpdateRequestStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    


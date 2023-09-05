"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional
from wingspan import utils

class AutoPayStrategyClientData(str, Enum):
    ALL = 'All'
    NONE = 'None'
    LESS_THAN_NIL_GREATER_THAN_ = '<nil>'

class VerificationStratgyClientData(str, Enum):
    NONE = 'None'
    ALL = 'All'
    LESS_THAN_NIL_GREATER_THAN_ = '<nil>'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ClientData:
    auto_pay_strategy: Optional[AutoPayStrategyClientData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('autoPayStrategy'), 'exclude': lambda f: f is None }})
    external_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('externalId'), 'exclude': lambda f: f is None }})
    verification_stratgy: Optional[VerificationStratgyClientData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('verificationStratgy'), 'exclude': lambda f: f is None }})
    


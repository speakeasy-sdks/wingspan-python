"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from typing import Optional
from wingspan import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class BankAccount:
    account_number: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountNumber') }})
    bank_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bankName') }})
    routing_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('routingNumber'), 'exclude': lambda f: f is None }})
    swift_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('swiftCode'), 'exclude': lambda f: f is None }})
    


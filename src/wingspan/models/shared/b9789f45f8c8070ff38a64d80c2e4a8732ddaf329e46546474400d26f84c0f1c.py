"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .memberclientform1099balances import MemberClientForm1099Balances
from dataclasses_json import Undefined, dataclass_json
from typing import Optional
from wingspan import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class B9789f45f8c8070ff38a64d80c2e4a8732ddaf329e46546474400d26f84c0f1c:
    two_thousand_and_twenty_one: Optional[MemberClientForm1099Balances] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('2021') }})
    two_thousand_and_twenty_two: Optional[MemberClientForm1099Balances] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('2022') }})
    


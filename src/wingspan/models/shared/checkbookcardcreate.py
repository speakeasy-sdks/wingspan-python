"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import address as shared_address
from dataclasses_json import Undefined, dataclass_json
from typing import Any, Optional, Union
from wingspan import utils



@dataclasses.dataclass
class CheckbookCardCreateAddress:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CheckbookCardCreate:
    card_number: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cardNumber') }})
    exp_mm: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expMM') }})
    exp_yyyy: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expYYYY') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    address: Optional[Union[Any, shared_address.Address]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address'), 'exclude': lambda f: f is None }})
    cvv: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cvv'), 'exclude': lambda f: f is None }})
    


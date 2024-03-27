"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from typing import Optional
from wingspan import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Sixad3f4f624fb518510130e879729b00ed8c237d1cebc5477abf34ac340a6424d:
    UNSET='__SPEAKEASY_UNSET__'
    expense_account_id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expenseAccountId'), 'exclude': lambda f: f is Sixad3f4f624fb518510130e879729b00ed8c237d1cebc5477abf34ac340a6424d.UNSET }})
    item_id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('itemId'), 'exclude': lambda f: f is Sixad3f4f624fb518510130e879729b00ed8c237d1cebc5477abf34ac340a6424d.UNSET }})
    


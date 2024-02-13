"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional
from wingspan import utils

class StatusScheduleDateUpdate(str, Enum):
    PENDING = 'Pending'
    COMPLETED = 'Completed'
    SKIPPED = 'Skipped'
    MODIFIED = 'Modified'
    LESS_THAN_NIL_GREATER_THAN_ = '<nil>'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ScheduleDateUpdate:
    UNSET='__SPEAKEASY_UNSET__'
    date_: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('date'), 'exclude': lambda f: f is ScheduleDateUpdate.UNSET }})
    invoice_template_id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceTemplateId'), 'exclude': lambda f: f is ScheduleDateUpdate.UNSET }})
    status: Optional[StatusScheduleDateUpdate] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is ScheduleDateUpdate.UNSET }})
    


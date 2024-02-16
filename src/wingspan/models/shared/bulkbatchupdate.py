"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Dict, Optional
from wingspan import utils

class StatusBulkBatchUpdate(str, Enum):
    OPEN = 'Open'
    PENDING = 'Pending'
    PROCESSING = 'Processing'
    COMPLETE = 'Complete'
    FAILED = 'Failed'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BulkBatchUpdate:
    UNSET='__SPEAKEASY_UNSET__'
    labels: Optional[Dict[str, str]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels'), 'exclude': lambda f: f is BulkBatchUpdate.UNSET }})
    status: Optional[StatusBulkBatchUpdate] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is BulkBatchUpdate.UNSET }})
    


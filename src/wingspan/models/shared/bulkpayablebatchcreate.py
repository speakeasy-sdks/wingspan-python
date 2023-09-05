"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional
from wingspan import utils

class BulkPayableBatchCreateProcessingStrategy(str, Enum):
    MERGE = 'Merge'
    SINGLE = 'Single'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class BulkPayableBatchCreate:
    processing_strategy: BulkPayableBatchCreateProcessingStrategy = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('processingStrategy') }})
    labels: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels'), 'exclude': lambda f: f is None }})
    


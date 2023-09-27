"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import frequencyupdate as shared_frequencyupdate
from dataclasses_json import Undefined, dataclass_json
from typing import Any, Optional, Union
from wingspan import utils



@dataclasses.dataclass
class LateFeeConfigUpdateFrequency:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class LateFeeConfigUpdate:
    frequency: Optional[Union[Any, shared_frequencyupdate.FrequencyUpdate]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('frequency'), 'exclude': lambda f: f is None }})
    late_fee_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lateFeeAmount'), 'exclude': lambda f: f is None }})
    late_fee_percentage: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lateFeePercentage'), 'exclude': lambda f: f is None }})
    


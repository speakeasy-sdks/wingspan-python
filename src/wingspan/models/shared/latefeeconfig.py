"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .frequency import Frequency
from dataclasses_json import Undefined, dataclass_json
from typing import Optional
from wingspan import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LateFeeConfig:
    UNSET='__SPEAKEASY_UNSET__'
    frequency: Frequency = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('frequency') }})
    late_fee_amount: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lateFeeAmount'), 'exclude': lambda f: f is LateFeeConfig.UNSET }})
    late_fee_percentage: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lateFeePercentage'), 'exclude': lambda f: f is LateFeeConfig.UNSET }})
    


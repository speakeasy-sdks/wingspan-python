"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .fee import Fee
from dataclasses_json import Undefined, dataclass_json
from typing import Optional
from wingspan import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Fees:
    UNSET='__SPEAKEASY_UNSET__'
    late_fee: Optional[Fee] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lateFee'), 'exclude': lambda f: f is Fees.UNSET }})
    processing_fee: Optional[Fee] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('processingFee'), 'exclude': lambda f: f is Fees.UNSET }})
    


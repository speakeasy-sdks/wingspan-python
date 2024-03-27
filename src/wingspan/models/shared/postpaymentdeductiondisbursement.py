"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from typing import Dict
from wingspan import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostPaymentDeductionDisbursement:
    inputs: Dict[str, str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('inputs') }})
    strategy: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('strategy') }})
    


"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from typing import Optional
from wingspan import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DeductionApplication:
    amount_deducted: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amountDeducted') }})
    payable_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payableId') }})
    disbursement_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('disbursementId') }})
    


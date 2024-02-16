"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Dict, Optional
from wingspan import utils

class CalculationTypeBulkCalculation1099ItemCreate(str, Enum):
    BALANCES = 'Balances'
    SUBMISSIONS = 'Submissions'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BulkCalculation1099ItemCreate:
    UNSET='__SPEAKEASY_UNSET__'
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientId') }})
    year: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('year') }})
    calculation_type: Optional[CalculationTypeBulkCalculation1099ItemCreate] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('calculationType'), 'exclude': lambda f: f is BulkCalculation1099ItemCreate.UNSET }})
    labels: Optional[Dict[str, str]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels'), 'exclude': lambda f: f is BulkCalculation1099ItemCreate.UNSET }})
    


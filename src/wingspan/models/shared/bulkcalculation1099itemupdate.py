"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional, Union
from wingspan import utils

class CalculationTypeBulkCalculation1099ItemUpdate(str, Enum):
    BALANCES = 'Balances'
    SUBMISSIONS = 'Submissions'
    LESS_THAN_NIL_GREATER_THAN_ = '<nil>'



@dataclasses.dataclass
class BulkCalculation1099ItemUpdateLabels:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class BulkCalculation1099ItemUpdate:
    calculation_type: Optional[CalculationTypeBulkCalculation1099ItemUpdate] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('calculationType'), 'exclude': lambda f: f is None }})
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientId'), 'exclude': lambda f: f is None }})
    labels: Optional[Union[Any, dict[str, str]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels'), 'exclude': lambda f: f is None }})
    year: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('year'), 'exclude': lambda f: f is None }})
    


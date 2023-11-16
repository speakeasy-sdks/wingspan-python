"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .facb8048736dba546c4c76242d9f8c7111011a7a7483528f37d80226698a1f2b import Facb8048736dba546c4c76242d9f8c7111011a7a7483528f37d80226698a1f2b
from .three_billion_one_hundred_and_ninety_million_six_hundred_and_eighty_five_thousand_eight_hundred_and_thirty_twoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461 import ThreeBillionOneHundredAndNinetyMillionSixHundredAndEightyFiveThousandEightHundredAndThirtyTwoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461
from dataclasses_json import Undefined, dataclass_json
from typing import Dict, Optional
from wingspan import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class InvoiceLineItemsCreateRequest:
    cost_per_unit: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('costPerUnit') }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description') }})
    detail: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('detail') }})
    discount: Optional[Facb8048736dba546c4c76242d9f8c7111011a7a7483528f37d80226698a1f2b] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('discount') }})
    integration: Optional[ThreeBillionOneHundredAndNinetyMillionSixHundredAndEightyFiveThousandEightHundredAndThirtyTwoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('integration') }})
    labels: Optional[Dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels') }})
    quantity: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quantity') }})
    reimbursable_expense: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reimbursableExpense') }})
    total_cost: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalCost') }})
    unit: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unit') }})
    


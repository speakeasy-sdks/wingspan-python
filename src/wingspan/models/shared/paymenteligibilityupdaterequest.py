"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from typing import Any, Optional, Union
from wingspan import utils



@dataclasses.dataclass
class PaymentEligibilityUpdateRequestValue2:
    pass



@dataclasses.dataclass
class PaymentEligibilityUpdateRequestValue:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PaymentEligibilityUpdateRequest:
    field: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('field') }})
    value: Optional[Union[Any, PaymentEligibilityUpdateRequestValue2]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value'), 'exclude': lambda f: f is None }})
    


"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import fee as shared_fee
from dataclasses_json import Undefined, dataclass_json
from typing import Any, Optional, Union
from wingspan import utils



@dataclasses.dataclass
class FeesLateFee:
    pass



@dataclasses.dataclass
class FeesProcessingFee:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class Fees:
    late_fee: Optional[Union[Any, shared_fee.Fee]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lateFee'), 'exclude': lambda f: f is None }})
    processing_fee: Optional[Union[Any, shared_fee.Fee]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('processingFee'), 'exclude': lambda f: f is None }})
    


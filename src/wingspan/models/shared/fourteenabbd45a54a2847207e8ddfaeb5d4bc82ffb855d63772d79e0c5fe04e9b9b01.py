"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from wingspan import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Fourteenabbd45a54a2847207e8ddfaeb5d4bc82ffb855d63772d79e0c5fe04e9b9b01:
    amount_withheld: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amountWithheld') }})
    rate: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rate') }})
    


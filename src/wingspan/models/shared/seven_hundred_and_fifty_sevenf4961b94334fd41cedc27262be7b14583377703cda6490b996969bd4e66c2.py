"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from wingspan import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SevenHundredAndFiftySevenf4961b94334fd41cedc27262be7b14583377703cda6490b996969bd4e66c2:
    items_failed: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('itemsFailed') }})
    items_processed: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('itemsProcessed') }})
    items_total: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('itemsTotal') }})
    


"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import sevenb49dbbd81f36ab6d7b4f07c5e2e53f40e36eb7b83d1488f379e993b830eec56 as shared_sevenb49dbbd81f36ab6d7b4f07c5e2e53f40e36eb7b83d1488f379e993b830eec56
from dataclasses_json import Undefined, dataclass_json
from typing import Optional
from wingspan import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class Remail1099Request:
    address: shared_sevenb49dbbd81f36ab6d7b4f07c5e2e53f40e36eb7b83d1488f379e993b830eec56.Sevenb49dbbd81f36ab6d7b4f07c5e2e53f40e36eb7b83d1488f379e993b830eec56 = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address') }})
    member_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberId') }})
    year: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('year') }})
    document_index: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('documentIndex'), 'exclude': lambda f: f is None }})
    

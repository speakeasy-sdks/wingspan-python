"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import sixb786d9a2229f84822749ed0e086e50a931cc189f3b1bfff2c851fae29b07879 as shared_sixb786d9a2229f84822749ed0e086e50a931cc189f3b1bfff2c851fae29b07879
from dataclasses_json import Undefined, dataclass_json
from typing import Optional
from wingspan import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Sixb94b58d661f3eabc1444a7a43ac4b99580f0d050123b7bf38184e2f0d7bd66e:
    quickbooks: Optional[shared_sixb786d9a2229f84822749ed0e086e50a931cc189f3b1bfff2c851fae29b07879.Sixb786d9a2229f84822749ed0e086e50a931cc189f3b1bfff2c851fae29b07879] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quickbooks') }})
    


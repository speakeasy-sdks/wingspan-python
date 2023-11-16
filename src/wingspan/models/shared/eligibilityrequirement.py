"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional
from wingspan import utils

class RequirementType(str, Enum):
    SIGNATURE = 'Signature'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EligibilityRequirement:
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientId') }})
    eligibility_requirement_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('eligibilityRequirementId') }})
    requirement_type: RequirementType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('requirementType') }})
    template_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('templateId') }})
    valid_for: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validFor') }})
    


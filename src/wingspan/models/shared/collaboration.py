"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .clientdata import ClientData
from .memberclientrequirementresponse import MemberClientRequirementResponse
from .twenty_sixe8ea23ccb1e007e7d6560175c7e75c768dac34727b7fe1d834ca24b8221ef4 import TwentySixe8ea23ccb1e007e7d6560175c7e75c768dac34727b7fe1d834ca24b8221ef4
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import List, Optional
from wingspan import utils

class StatusCollaboration(str, Enum):
    ACTIVE = 'Active'
    INACTIVE = 'Inactive'
    PENDING = 'Pending'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Collaboration:
    collaborator_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collaboratorId') }})
    status: StatusCollaboration = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    client_data: Optional[ClientData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientData') }})
    collaborator_group_ids: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collaboratorGroupIds') }})
    eligibility_requirements: Optional[List[MemberClientRequirementResponse]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('eligibilityRequirements') }})
    integration: Optional[TwentySixe8ea23ccb1e007e7d6560175c7e75c768dac34727b7fe1d834ca24b8221ef4] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('integration') }})
    


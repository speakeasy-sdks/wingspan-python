"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import documentresponse as shared_documentresponse
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional, Union
from wingspan import utils



@dataclasses.dataclass
class MemberClientRequirementResponseDocument:
    pass

class MemberClientRequirementResponseRequirementType(str, Enum):
    SIGNATURE = 'Signature'

class StatusMemberClientRequirementResponse(str, Enum):
    NEW = 'New'
    SENT = 'Sent'
    PENDING = 'Pending'
    COMPLETE = 'Complete'
    LESS_THAN_NIL_GREATER_THAN_ = '<nil>'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class MemberClientRequirementResponse:
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientId') }})
    collaborator_group_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collaboratorGroupId') }})
    eligibility_requirement_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('eligibilityRequirementId') }})
    requirement_type: MemberClientRequirementResponseRequirementType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('requirementType') }})
    document: Optional[Union[Any, shared_documentresponse.DocumentResponse]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('document'), 'exclude': lambda f: f is None }})
    document_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('documentId'), 'exclude': lambda f: f is None }})
    status: Optional[StatusMemberClientRequirementResponse] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    template_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('templateId'), 'exclude': lambda f: f is None }})
    valid_for: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validFor'), 'exclude': lambda f: f is None }})
    


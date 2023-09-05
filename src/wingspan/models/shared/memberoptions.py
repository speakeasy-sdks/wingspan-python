"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional
from wingspan import utils

class PayoutPreferencesMemberOptions(str, Enum):
    STANDARD = 'Standard'
    INSTANT = 'Instant'
    EXPEDITED = 'Expedited'
    CHECK = 'Check'
    E_CHECK = 'ECheck'
    LESS_THAN_NIL_GREATER_THAN_ = '<nil>'

class WorkflowStatusMemberOptions(str, Enum):
    DISPUTED = 'Disputed'
    ACCEPTED = 'Accepted'
    RESUBMITTED = 'Resubmitted'
    LESS_THAN_NIL_GREATER_THAN_ = '<nil>'

class WorkflowSubStatusMemberOptions(str, Enum):
    SUBMITTED = 'Submitted'
    LESS_THAN_NIL_GREATER_THAN_ = '<nil>'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class MemberOptions:
    comment: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('comment'), 'exclude': lambda f: f is None }})
    payout_preferences: Optional[PayoutPreferencesMemberOptions] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payoutPreferences'), 'exclude': lambda f: f is None }})
    workflow_status: Optional[WorkflowStatusMemberOptions] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workflowStatus'), 'exclude': lambda f: f is None }})
    workflow_sub_status: Optional[WorkflowSubStatusMemberOptions] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workflowSubStatus'), 'exclude': lambda f: f is None }})
    

"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional
from wingspan import utils

class WorkflowStatusClientOptions(str, Enum):
    PENDING = 'Pending'
    PRE_APPROVED = 'PreApproved'
    APPROVED = 'Approved'
    PAYMENT_INITIATED = 'PaymentInitiated'
    FUNDED = 'Funded'
    DECLINED = 'Declined'
    LESS_THAN_NIL_GREATER_THAN_ = '<nil>'

class WorkflowSubStatusClientOptions(str, Enum):
    SUBMITTED = 'Submitted'
    LESS_THAN_NIL_GREATER_THAN_ = '<nil>'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ClientOptions:
    comment: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('comment'), 'exclude': lambda f: f is None }})
    pay_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payDate'), 'exclude': lambda f: f is None }})
    workflow_status: Optional[WorkflowStatusClientOptions] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workflowStatus'), 'exclude': lambda f: f is None }})
    workflow_sub_status: Optional[WorkflowSubStatusClientOptions] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workflowSubStatus'), 'exclude': lambda f: f is None }})
    


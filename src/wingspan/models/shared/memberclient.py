"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import b9789f45f8c8070ff38a64d80c2e4a8732ddaf329e46546474400d26f84c0f1c as shared_b9789f45f8c8070ff38a64d80c2e4a8732ddaf329e46546474400d26f84c0f1c
from ..shared import clientdata as shared_clientdata
from ..shared import externalids as shared_externalids
from ..shared import fifty_foura6b24a57d15569713a0fc2cbf4d7b60e5b00c0035643d120b72001060ebd30 as shared_fifty_foura6b24a57d15569713a0fc2cbf4d7b60e5b00c0035643d120b72001060ebd30
from ..shared import memberclientformw9info as shared_memberclientformw9info
from ..shared import memberclientwireaccount as shared_memberclientwireaccount
from ..shared import memberdata as shared_memberdata
from ..shared import redactedmember as shared_redactedmember
from ..shared import userroles as shared_userroles
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional
from wingspan import utils

class StatusMemberClient(str, Enum):
    ACTIVE = 'Active'
    INACTIVE = 'Inactive'
    PENDING = 'Pending'

class TaxStatusMemberClient(str, Enum):
    COMPLETE = 'Complete'
    FAILED = 'Failed'
    PENDING = 'Pending'
    INCOMPLETE = 'Incomplete'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class MemberClient:
    ach_credit_account: shared_memberclientwireaccount.MemberClientWireAccount = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('achCreditAccount') }})
    client: shared_redactedmember.RedactedMember = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client') }})
    client_data: shared_clientdata.ClientData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientData') }})
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientId') }})
    created_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt') }})
    email_to: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('emailTo') }})
    external_ids: shared_externalids.ExternalIds = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('externalIds') }})
    form1099_balances: shared_b9789f45f8c8070ff38a64d80c2e4a8732ddaf329e46546474400d26f84c0f1c.B9789f45f8c8070ff38a64d80c2e4a8732ddaf329e46546474400d26f84c0f1c = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('form1099Balances') }})
    form_w9_data: shared_memberclientformw9info.MemberClientFormW9Info = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('formW9Data') }})
    internal: shared_fifty_foura6b24a57d15569713a0fc2cbf4d7b60e5b00c0035643d120b72001060ebd30.FiftyFoura6b24a57d15569713a0fc2cbf4d7b60e5b00c0035643d120b72001060ebd30 = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('internal') }})
    international_wire_account: shared_memberclientwireaccount.MemberClientWireAccount = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('internationalWireAccount') }})
    labels: dict[str, str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels') }})
    member: shared_redactedmember.RedactedMember = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('member') }})
    member_client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberClientId') }})
    member_data: shared_memberdata.MemberData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberData') }})
    member_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberId') }})
    status: StatusMemberClient = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    tax_status: TaxStatusMemberClient = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxStatus') }})
    updated_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt') }})
    user_roles: shared_userroles.UserRoles = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userRoles') }})
    collaborator_group_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collaboratorGroupId'), 'exclude': lambda f: f is None }})
    collaborator_group_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collaboratorGroupIds'), 'exclude': lambda f: f is None }})
    company: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('company'), 'exclude': lambda f: f is None }})
    eligibility_requirements: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('eligibilityRequirements'), 'exclude': lambda f: f is None }})
    email_cc: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('emailCC'), 'exclude': lambda f: f is None }})
    integration: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('integration'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    

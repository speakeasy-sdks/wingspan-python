"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .b9789f45f8c8070ff38a64d80c2e4a8732ddaf329e46546474400d26f84c0f1c import B9789f45f8c8070ff38a64d80c2e4a8732ddaf329e46546474400d26f84c0f1c
from .memberclientrequirementresponse import MemberClientRequirementResponse
from .memberclientwireaccount import MemberClientWireAccount
from .redactedmember import RedactedMember
from .threed33fba3f009de957b3be92fba006d6383af7e39f823cc1fd213506f6205100f import Threed33fba3f009de957b3be92fba006d6383af7e39f823cc1fd213506f6205100f
from .userroles import UserRoles
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Dict, List, Optional
from wingspan import utils

class StatusMemberClientSchema(str, Enum):
    ACTIVE = 'Active'
    INACTIVE = 'Inactive'
    PENDING = 'Pending'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class MemberClientSchema:
    ach_credit_account: MemberClientWireAccount = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('achCreditAccount') }})
    client: RedactedMember = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client') }})
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientId') }})
    created_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt') }})
    email_to: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('emailTo') }})
    form1099_balances: B9789f45f8c8070ff38a64d80c2e4a8732ddaf329e46546474400d26f84c0f1c = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('form1099Balances') }})
    international_wire_account: MemberClientWireAccount = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('internationalWireAccount') }})
    labels: Dict[str, str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels') }})
    member_client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberClientId') }})
    status: StatusMemberClientSchema = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    updated_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt') }})
    user_roles: UserRoles = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userRoles') }})
    collaborator_group_ids: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collaboratorGroupIds') }})
    company: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('company') }})
    eligibility_requirements: Optional[List[MemberClientRequirementResponse]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('eligibilityRequirements') }})
    email_cc: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('emailCC') }})
    integration: Optional[Threed33fba3f009de957b3be92fba006d6383af7e39f823cc1fd213506f6205100f] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('integration') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    


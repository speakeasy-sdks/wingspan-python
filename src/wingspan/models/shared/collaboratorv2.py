"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import b9789f45f8c8070ff38a64d80c2e4a8732ddaf329e46546474400d26f84c0f1c as shared_b9789f45f8c8070ff38a64d80c2e4a8732ddaf329e46546474400d26f84c0f1c
from ..shared import clientdata as shared_clientdata
from ..shared import collaboration as shared_collaboration
from ..shared import collaboratorevents as shared_collaboratorevents
from ..shared import collaboratorv2formw9info as shared_collaboratorv2formw9info
from ..shared import memberclientwireaccount as shared_memberclientwireaccount
from ..shared import memberdata as shared_memberdata
from ..shared import ninecd48bf78a297540b0ec6f45365beb8d6ce0ee88e6d244115ad226e6701011a3 as shared_ninecd48bf78a297540b0ec6f45365beb8d6ce0ee88e6d244115ad226e6701011a3
from ..shared import redactedmember as shared_redactedmember
from ..shared import userroles as shared_userroles
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Dict, List, Optional
from wingspan import utils

class StatusCollaboratorV2(str, Enum):
    ACTIVE = 'Active'
    INACTIVE = 'Inactive'
    PENDING = 'Pending'

class TaxStatusCollaboratorV2(str, Enum):
    COMPLETE = 'Complete'
    FAILED = 'Failed'
    PENDING = 'Pending'
    INCOMPLETE = 'Incomplete'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CollaboratorV2:
    ach_credit_account: shared_memberclientwireaccount.MemberClientWireAccount = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('achCreditAccount') }})
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientId') }})
    collaborations: List[shared_collaboration.Collaboration] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collaborations') }})
    created_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt') }})
    first_collaboration_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('firstCollaborationId') }})
    form1099_balances: shared_b9789f45f8c8070ff38a64d80c2e4a8732ddaf329e46546474400d26f84c0f1c.B9789f45f8c8070ff38a64d80c2e4a8732ddaf329e46546474400d26f84c0f1c = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('form1099Balances') }})
    form_w9_data: shared_collaboratorv2formw9info.CollaboratorV2FormW9Info = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('formW9Data') }})
    internal: shared_ninecd48bf78a297540b0ec6f45365beb8d6ce0ee88e6d244115ad226e6701011a3.Ninecd48bf78a297540b0ec6f45365beb8d6ce0ee88e6d244115ad226e6701011a3 = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('internal') }})
    international_wire_account: shared_memberclientwireaccount.MemberClientWireAccount = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('internationalWireAccount') }})
    labels: Dict[str, str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels') }})
    member: shared_redactedmember.RedactedMember = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('member') }})
    member_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberId') }})
    primary_collaboration_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('primaryCollaborationId') }})
    status: StatusCollaboratorV2 = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    tax_status: TaxStatusCollaboratorV2 = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxStatus') }})
    updated_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt') }})
    user_roles: shared_userroles.UserRoles = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userRoles') }})
    client_data: Optional[shared_clientdata.ClientData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientData') }})
    member_data: Optional[shared_memberdata.MemberData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberData') }})
    member_events: Optional[shared_collaboratorevents.CollaboratorEvents] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberEvents') }})
    


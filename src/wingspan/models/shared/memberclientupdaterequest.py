"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import clientdata as shared_clientdata
from ..shared import memberdata as shared_memberdata
from ..shared import ninetyf96495b02c2509fff131505484d46479a91b7d23ed2b0f438ca117d0bccad7 as shared_ninetyf96495b02c2509fff131505484d46479a91b7d23ed2b0f438ca117d0bccad7
from ..shared import threed33fba3f009de957b3be92fba006d6383af7e39f823cc1fd213506f6205100f as shared_threed33fba3f009de957b3be92fba006d6383af7e39f823cc1fd213506f6205100f
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Dict, List, Optional
from wingspan import utils


@dataclasses.dataclass
class MemberClientUpdateRequestFormW9Data:
    pass

class StatusMemberClientUpdateRequest(str, Enum):
    ACTIVE = 'Active'
    INACTIVE = 'Inactive'
    PENDING = 'Pending'
    LESS_THAN_NIL_GREATER_THAN_ = '<nil>'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class MemberClientUpdateRequest:
    client_data: Optional[shared_clientdata.ClientData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientData') }})
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientId') }})
    company: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('company') }})
    email_cc: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('emailCC') }})
    email_to: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('emailTo') }})
    form1099_balances: Optional[shared_ninetyf96495b02c2509fff131505484d46479a91b7d23ed2b0f438ca117d0bccad7.Ninetyf96495b02c2509fff131505484d46479a91b7d23ed2b0f438ca117d0bccad7] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('form1099Balances') }})
    form_w9_data: Optional[MemberClientUpdateRequestFormW9Data] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('formW9Data') }})
    integration: Optional[shared_threed33fba3f009de957b3be92fba006d6383af7e39f823cc1fd213506f6205100f.Threed33fba3f009de957b3be92fba006d6383af7e39f823cc1fd213506f6205100f] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('integration') }})
    labels: Optional[Dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels') }})
    member_data: Optional[shared_memberdata.MemberData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberData') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    status: Optional[StatusMemberClientUpdateRequest] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    


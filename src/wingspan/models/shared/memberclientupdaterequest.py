"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .clientdata import ClientData
from .memberdata import MemberData
from .ninetyf96495b02c2509fff131505484d46479a91b7d23ed2b0f438ca117d0bccad7 import Ninetyf96495b02c2509fff131505484d46479a91b7d23ed2b0f438ca117d0bccad7
from .threed33fba3f009de957b3be92fba006d6383af7e39f823cc1fd213506f6205100f import Threed33fba3f009de957b3be92fba006d6383af7e39f823cc1fd213506f6205100f
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


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class MemberClientUpdateRequest:
    UNSET='__SPEAKEASY_UNSET__'
    client_data: Optional[ClientData] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientData'), 'exclude': lambda f: f is MemberClientUpdateRequest.UNSET }})
    client_id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientId'), 'exclude': lambda f: f is MemberClientUpdateRequest.UNSET }})
    company: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('company'), 'exclude': lambda f: f is MemberClientUpdateRequest.UNSET }})
    email_cc: Optional[List[str]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('emailCC'), 'exclude': lambda f: f is MemberClientUpdateRequest.UNSET }})
    email_to: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('emailTo'), 'exclude': lambda f: f is MemberClientUpdateRequest.UNSET }})
    form1099_balances: Optional[Ninetyf96495b02c2509fff131505484d46479a91b7d23ed2b0f438ca117d0bccad7] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('form1099Balances'), 'exclude': lambda f: f is MemberClientUpdateRequest.UNSET }})
    form_w9_data: Optional[MemberClientUpdateRequestFormW9Data] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('formW9Data'), 'exclude': lambda f: f is MemberClientUpdateRequest.UNSET }})
    integration: Optional[Threed33fba3f009de957b3be92fba006d6383af7e39f823cc1fd213506f6205100f] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('integration'), 'exclude': lambda f: f is MemberClientUpdateRequest.UNSET }})
    labels: Optional[Dict[str, str]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels'), 'exclude': lambda f: f is MemberClientUpdateRequest.UNSET }})
    member_data: Optional[MemberData] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberData'), 'exclude': lambda f: f is MemberClientUpdateRequest.UNSET }})
    name: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is MemberClientUpdateRequest.UNSET }})
    status: Optional[StatusMemberClientUpdateRequest] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is MemberClientUpdateRequest.UNSET }})
    


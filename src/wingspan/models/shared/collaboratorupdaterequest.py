"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .clientdata import ClientData
from .ninetyf96495b02c2509fff131505484d46479a91b7d23ed2b0f438ca117d0bccad7 import Ninetyf96495b02c2509fff131505484d46479a91b7d23ed2b0f438ca117d0bccad7
from .twenty_sixe8ea23ccb1e007e7d6560175c7e75c768dac34727b7fe1d834ca24b8221ef4 import TwentySixe8ea23ccb1e007e7d6560175c7e75c768dac34727b7fe1d834ca24b8221ef4
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Dict, Optional
from wingspan import utils


@dataclasses.dataclass
class FormW9Data:
    pass

class StatusCollaboratorUpdateRequest(str, Enum):
    ACTIVE = 'Active'
    INACTIVE = 'Inactive'
    PENDING = 'Pending'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CollaboratorUpdateRequest:
    UNSET='__SPEAKEASY_UNSET__'
    client_data: Optional[ClientData] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientData'), 'exclude': lambda f: f is CollaboratorUpdateRequest.UNSET }})
    form1099_balances: Optional[Ninetyf96495b02c2509fff131505484d46479a91b7d23ed2b0f438ca117d0bccad7] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('form1099Balances'), 'exclude': lambda f: f is CollaboratorUpdateRequest.UNSET }})
    form_w9_data: Optional[FormW9Data] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('formW9Data'), 'exclude': lambda f: f is CollaboratorUpdateRequest.UNSET }})
    integration: Optional[TwentySixe8ea23ccb1e007e7d6560175c7e75c768dac34727b7fe1d834ca24b8221ef4] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('integration'), 'exclude': lambda f: f is CollaboratorUpdateRequest.UNSET }})
    labels: Optional[Dict[str, str]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels'), 'exclude': lambda f: f is CollaboratorUpdateRequest.UNSET }})
    status: Optional[StatusCollaboratorUpdateRequest] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is CollaboratorUpdateRequest.UNSET }})
    


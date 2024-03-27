"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .payoutdestinationupdate import PayoutDestinationUpdate
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import List, Optional
from wingspan import utils

class PayoutPreferencesPayoutSettingsUpdate(str, Enum):
    STANDARD = 'Standard'
    INSTANT = 'Instant'
    EXPEDITED = 'Expedited'
    CHECK = 'Check'
    E_CHECK = 'ECheck'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PayoutSettingsUpdate:
    UNSET='__SPEAKEASY_UNSET__'
    payout_destinations: Optional[List[PayoutDestinationUpdate]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payoutDestinations'), 'exclude': lambda f: f is PayoutSettingsUpdate.UNSET }})
    payout_preferences: Optional[PayoutPreferencesPayoutSettingsUpdate] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payoutPreferences'), 'exclude': lambda f: f is PayoutSettingsUpdate.UNSET }})
    


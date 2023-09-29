"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import ce853dbef33b2b91880690c84bc5314340c1301fd7b3503dd6ce79c844e2a481 as shared_ce853dbef33b2b91880690c84bc5314340c1301fd7b3503dd6ce79c844e2a481
from ..shared import eighta9c6cb49482a98cdd603ff09858cdc3e5ef6ad9807c876c4161d925a96694a5 as shared_eighta9c6cb49482a98cdd603ff09858cdc3e5ef6ad9807c876c4161d925a96694a5
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional, Union
from wingspan import utils



@dataclasses.dataclass
class CollaboratorForm1099BalancesUpdateRequestCorrection:
    pass

class DeliveryMethodCollaboratorForm1099BalancesUpdateRequest(str, Enum):
    ELECTRONIC = 'Electronic'
    MAIL = 'Mail'
    BOTH = 'Both'
    LESS_THAN_NIL_GREATER_THAN_ = '<nil>'



@dataclasses.dataclass
class CollaboratorForm1099BalancesUpdateRequestDispute:
    pass



@dataclasses.dataclass
class CollaboratorForm1099BalancesUpdateRequestEvents2:
    pass



@dataclasses.dataclass
class CollaboratorForm1099BalancesUpdateRequestEvents:
    pass

class StatusCollaboratorForm1099BalancesUpdateRequest(str, Enum):
    READY = 'Ready'
    NEEDS_ACTION_INFO = 'NeedsActionInfo'
    NEEDS_ACTION_DISPUTE = 'NeedsActionDispute'
    SUBMITTED = 'Submitted'
    REJECTED = 'Rejected'
    ACCEPTED = 'Accepted'
    EXCLUDED = 'Excluded'
    LESS_THAN_NIL_GREATER_THAN_ = '<nil>'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CollaboratorForm1099BalancesUpdateRequest:
    adjustments: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('adjustments') }})
    correction: Optional[Union[Any, shared_ce853dbef33b2b91880690c84bc5314340c1301fd7b3503dd6ce79c844e2a481.Ce853dbef33b2b91880690c84bc5314340c1301fd7b3503dd6ce79c844e2a481]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('correction'), 'exclude': lambda f: f is None }})
    delivery_method: Optional[DeliveryMethodCollaboratorForm1099BalancesUpdateRequest] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deliveryMethod') }})
    dispute: Optional[Union[Any, shared_eighta9c6cb49482a98cdd603ff09858cdc3e5ef6ad9807c876c4161d925a96694a5.Eighta9c6cb49482a98cdd603ff09858cdc3e5ef6ad9807c876c4161d925a96694a5]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dispute'), 'exclude': lambda f: f is None }})
    events: Optional[Union[Any, CollaboratorForm1099BalancesUpdateRequestEvents2]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('events'), 'exclude': lambda f: f is None }})
    status: Optional[StatusCollaboratorForm1099BalancesUpdateRequest] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    


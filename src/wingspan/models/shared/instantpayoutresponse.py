"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import fundstransferaccount as shared_fundstransferaccount
from dataclasses_json import Undefined, dataclass_json
from wingspan import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class InstantPayoutResponse:
    instant_payout_account: shared_fundstransferaccount.FundsTransferAccount = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instantPayoutAccount') }})
    instant_payout_account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instantPayoutAccountId') }})
    


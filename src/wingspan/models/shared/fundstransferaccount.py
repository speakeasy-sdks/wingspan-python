"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import eight_thousand_two_hundred_and_twelveee55b9e13fc32935c9417826f64b3550a203b665a04aacb02c4cac363c1f as shared_eight_thousand_two_hundred_and_twelveee55b9e13fc32935c9417826f64b3550a203b665a04aacb02c4cac363c1f
from ..shared import thirty_fivee19f440b766b63a803909f93debbd6971f4c581457e6e66b0b7313eed6ccbc as shared_thirty_fivee19f440b766b63a803909f93debbd6971f4c581457e6e66b0b7313eed6ccbc
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional
from wingspan import utils

class CurrencyFundsTransferAccount(str, Enum):
    USD = 'USD'
    CAD = 'CAD'

class TypeFundsTransferAccount(str, Enum):
    CARD = 'Card'
    BANK_ACCOUNT = 'BankAccount'
    INTERNAL_ACCOUNT = 'InternalAccount'
    STRIPE_ACCOUNT = 'StripeAccount'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class FundsTransferAccount:
    country: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country') }})
    currency: CurrencyFundsTransferAccount = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency') }})
    holder_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('holderName') }})
    internal: shared_thirty_fivee19f440b766b63a803909f93debbd6971f4c581457e6e66b0b7313eed6ccbc.ThirtyFivee19f440b766b63a803909f93debbd6971f4c581457e6e66b0b7313eed6ccbc = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('internal') }})
    numbers: shared_eight_thousand_two_hundred_and_twelveee55b9e13fc32935c9417826f64b3550a203b665a04aacb02c4cac363c1f.EightThousandTwoHundredAndTwelveee55b9e13fc32935c9417826f64b3550a203b665a04aacb02c4cac363c1f = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('numbers') }})
    type: TypeFundsTransferAccount = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    user_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userId') }})
    


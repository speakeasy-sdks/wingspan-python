"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional
from wingspan import utils

class DestinationTypeInvoicePayoutDestination(str, Enum):
    ACCOUNT = 'Account'
    CARD = 'Card'
    INTERNAL_ACCOUNT = 'InternalAccount'
    PAPER_CHECK = 'PaperCheck'
    WE_GIFT = 'WeGift'

class PayoutMethodInvoicePayoutDestination(str, Enum):
    STANDARD = 'Standard'
    INSTANT = 'Instant'
    EXPEDITED = 'Expedited'
    CHECK = 'Check'
    E_CHECK = 'ECheck'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class InvoicePayoutDestination:
    amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount') }})
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description') }})
    destination_type: DestinationTypeInvoicePayoutDestination = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})
    payout_method: PayoutMethodInvoicePayoutDestination = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payoutMethod') }})
    percentage: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('percentage') }})
    transfer_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transferId') }})
    brand: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('brand') }})
    destination_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationId') }})
    last4: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last4') }})
    


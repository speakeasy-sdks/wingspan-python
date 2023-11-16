"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional
from wingspan import utils

class MeansTypePaymentInfo(str, Enum):
    CARD = 'Card'
    ACCOUNT = 'Account'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PaymentInfo:
    means_type: MeansTypePaymentInfo = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('meansType') }})
    brand_image_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('brandImageUrl') }})
    card_brand: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cardBrand') }})
    means_description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('meansDescription') }})
    means_last4: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('meansLast4') }})
    


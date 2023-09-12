"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from wingspan import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CardCodeResponse:
    phone_number: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phoneNumber') }})
    verification_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('verificationToken') }})
    


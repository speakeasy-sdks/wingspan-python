"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from wingspan import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class InstitutionResponse:
    address: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address') }})
    is_ach_supported: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isACHSupported') }})
    is_rtp_supported: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isRTPSupported') }})
    is_wire_supported: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isWireSupported') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    routing_number: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('routingNumber') }})
    


"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional
from wingspan import utils

class CompanyStructureCollaboratorV2FormW9Info(str, Enum):
    NONE = 'None'
    SOLE_PROPRIETORSHIP = 'SoleProprietorship'
    LLC_SINGLE_MEMBER = 'LlcSingleMember'
    LLC_MULTI_MEMBER = 'LlcMultiMember'
    CORPORATION_S = 'CorporationS'
    LLC_CORPORATION_S = 'LLCCorporationS'
    LLC_CORPORATION_C = 'LLCCorporationC'
    LLC_PARTNERSHIP = 'LLCPartnership'
    CORPORATION_C = 'CorporationC'
    PARTNERSHIP = 'Partnership'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CollaboratorV2FormW9Info:
    address_line1: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('addressLine1') }})
    city: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('city') }})
    company_structure: CompanyStructureCollaboratorV2FormW9Info = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('companyStructure') }})
    country: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country') }})
    postal_code: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('postalCode') }})
    state: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('state') }})
    address_line2: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('addressLine2') }})
    dob: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dob') }})
    ein: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ein') }})
    first_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('firstName') }})
    last_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lastName') }})
    legal_business_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('legalBusinessName') }})
    ssn_last_four: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssnLastFour') }})
    


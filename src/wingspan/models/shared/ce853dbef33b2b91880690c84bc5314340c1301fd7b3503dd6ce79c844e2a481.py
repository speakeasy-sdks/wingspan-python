"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional
from wingspan import utils



@dataclasses.dataclass
class Ce853dbef33b2b91880690c84bc5314340c1301fd7b3503dd6ce79c844e2a481Address2:
    pass

class CompanyStructurece853dbef33b2b91880690c84bc5314340c1301fd7b3503dd6ce79c844e2a481(str, Enum):
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
    LESS_THAN_NIL_GREATER_THAN_ = '<nil>'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class Ce853dbef33b2b91880690c84bc5314340c1301fd7b3503dd6ce79c844e2a481:
    address: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address'), 'exclude': lambda f: f is None }})
    company_structure: Optional[CompanyStructurece853dbef33b2b91880690c84bc5314340c1301fd7b3503dd6ce79c844e2a481] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('companyStructure'), 'exclude': lambda f: f is None }})
    ein: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ein'), 'exclude': lambda f: f is None }})
    first_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('firstName'), 'exclude': lambda f: f is None }})
    last_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lastName'), 'exclude': lambda f: f is None }})
    legal_business_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('legalBusinessName'), 'exclude': lambda f: f is None }})
    ssn: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssn'), 'exclude': lambda f: f is None }})
    total_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalAmount'), 'exclude': lambda f: f is None }})
    


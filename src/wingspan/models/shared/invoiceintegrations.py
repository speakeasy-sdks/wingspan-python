"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import sixa889960fef25bc170d22a40a86ac4d6889f536685dd9369ec52d3df36732601 as shared_sixa889960fef25bc170d22a40a86ac4d6889f536685dd9369ec52d3df36732601
from dataclasses_json import Undefined, dataclass_json
from typing import Optional
from wingspan import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class InvoiceIntegrations:
    quickbooks: Optional[shared_sixa889960fef25bc170d22a40a86ac4d6889f536685dd9369ec52d3df36732601.Sixa889960fef25bc170d22a40a86ac4d6889f536685dd9369ec52d3df36732601] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quickbooks') }})
    


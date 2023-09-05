"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from typing import Optional
from wingspan import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CollaboratorEvents:
    r"""List of events on collaborator"""
    know_your_customer_verified_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('knowYourCustomerVerifiedAt') }})
    payout_method_first_added_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payoutMethodFirstAddedAt') }})
    tax_documentation_verified_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxDocumentationVerifiedAt') }})
    signed_up_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('signedUpAt'), 'exclude': lambda f: f is None }})
    

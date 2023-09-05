"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from wingspan import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class InvoiceAmountDetails:
    client_paid: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientPaid') }})
    collaborator_payments: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collaboratorPayments') }})
    deductions: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deductions') }})
    member_gross: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberGross') }})
    member_net: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberNet') }})
    member_tax_withheld: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberTaxWithheld') }})
    processing_fee: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('processingFee') }})
    wingspan_top_up: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('wingspanTopUp') }})
    


"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import deductionapplication as shared_deductionapplication
from ..shared import postpaymentdeductiondisbursement as shared_postpaymentdeductiondisbursement
from ..shared import userroles as shared_userroles
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Dict, List, Optional
from wingspan import utils

class CurrencyDeductionResponse(str, Enum):
    USD = 'USD'
    CAD = 'CAD'

class DeductionResponseStatus(str, Enum):
    PENDING = 'Pending'
    PARTIALLY_APPLIED = 'PartiallyApplied'
    COMPLETE = 'Complete'

class TypeDeductionResponse(str, Enum):
    PRE_PAYMENT = 'PrePayment'
    POST_PAYMENT = 'PostPayment'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeductionResponse:
    amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount') }})
    application: List[shared_deductionapplication.DeductionApplication] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('application') }})
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientId') }})
    created_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt') }})
    currency: CurrencyDeductionResponse = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency') }})
    deduction_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deductionId') }})
    labels: Dict[str, str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels') }})
    member_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberId') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    priority: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('priority') }})
    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('startDate') }})
    status: DeductionResponseStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    type: TypeDeductionResponse = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    updated_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt') }})
    user_roles: shared_userroles.UserRoles = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userRoles') }})
    deduction_template_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deductionTemplateId') }})
    disbursement: Optional[shared_postpaymentdeductiondisbursement.PostPaymentDeductionDisbursement] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('disbursement') }})
    source_invoice_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceInvoiceId') }})
    


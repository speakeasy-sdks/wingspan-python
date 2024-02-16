"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .feehandlingconfig import FeeHandlingConfig
from .invoicelineitemscreaterequest import InvoiceLineItemsCreateRequest
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import List, Optional
from wingspan import utils

class CurrencyClientInvoiceCreateRequest(str, Enum):
    USD = 'USD'
    CAD = 'CAD'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ClientInvoiceCreateRequest:
    UNSET='__SPEAKEASY_UNSET__'
    client_email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientEmail') }})
    due_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dueDate') }})
    line_items: List[InvoiceLineItemsCreateRequest] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lineItems') }})
    member_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberId') }})
    client_company: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientCompany'), 'exclude': lambda f: f is ClientInvoiceCreateRequest.UNSET }})
    client_email_cc: Optional[List[str]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientEmailCC'), 'exclude': lambda f: f is ClientInvoiceCreateRequest.UNSET }})
    client_first_name: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientFirstName'), 'exclude': lambda f: f is ClientInvoiceCreateRequest.UNSET }})
    client_last_name: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientLastName'), 'exclude': lambda f: f is ClientInvoiceCreateRequest.UNSET }})
    credit_fee_handling: Optional[FeeHandlingConfig] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('creditFeeHandling'), 'exclude': lambda f: f is ClientInvoiceCreateRequest.UNSET }})
    currency: Optional[CurrencyClientInvoiceCreateRequest] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency'), 'exclude': lambda f: f is ClientInvoiceCreateRequest.UNSET }})
    


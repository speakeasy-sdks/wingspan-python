"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import calculationsettings1099 as shared_calculationsettings1099
from ..shared import frequencyupdate as shared_frequencyupdate
from ..shared import fundingsource as shared_fundingsource
from ..shared import scheduledateupdate as shared_scheduledateupdate
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import List, Optional
from wingspan import utils

class StatusPayrollSettingsUpdate(str, Enum):
    ACTIVE = 'Active'
    DRAFT = 'Draft'
    EXPIRED = 'Expired'
    CANCELLED = 'Cancelled'
    LESS_THAN_NIL_GREATER_THAN_ = '<nil>'

class WorkflowPayrollSettingsUpdate(str, Enum):
    SINGLE_STAGE = 'SingleStage'
    DUAL_STAGE = 'DualStage'
    LESS_THAN_NIL_GREATER_THAN_ = '<nil>'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PayrollSettingsUpdate:
    calculation_settings1099: Optional[shared_calculationsettings1099.CalculationSettings1099] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('calculationSettings1099') }})
    enable_planned_payroll: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enablePlannedPayroll') }})
    enable_process_days_before_due: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enableProcessDaysBeforeDue') }})
    frequency: Optional[shared_frequencyupdate.FrequencyUpdate] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('frequency') }})
    funding_source: Optional[shared_fundingsource.FundingSource] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fundingSource') }})
    issue1099s: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('issue1099s') }})
    process_days_before_due: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('processDaysBeforeDue') }})
    schedule_dates: Optional[List[shared_scheduledateupdate.ScheduleDateUpdate]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scheduleDates') }})
    status: Optional[StatusPayrollSettingsUpdate] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    workflow: Optional[WorkflowPayrollSettingsUpdate] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workflow') }})
    


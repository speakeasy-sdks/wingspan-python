"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .calculationsettings1099 import CalculationSettings1099
from .frequency import Frequency
from .fundingsource import FundingSource
from .scheduledate import ScheduleDate
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import List, Optional
from wingspan import utils

class StatusPayrollSettings(str, Enum):
    ACTIVE = 'Active'
    DRAFT = 'Draft'
    EXPIRED = 'Expired'
    CANCELLED = 'Cancelled'

class Workflow(str, Enum):
    SINGLE_STAGE = 'SingleStage'
    DUAL_STAGE = 'DualStage'
    LESS_THAN_NIL_GREATER_THAN_ = '<nil>'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PayrollSettings:
    status: StatusPayrollSettings = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    calculation_settings1099: Optional[CalculationSettings1099] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('calculationSettings1099') }})
    enable_planned_payroll: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enablePlannedPayroll') }})
    enable_process_days_before_due: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enableProcessDaysBeforeDue') }})
    frequency: Optional[Frequency] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('frequency') }})
    funding_source: Optional[FundingSource] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fundingSource') }})
    issue1099s: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('issue1099s') }})
    process_days_before_due: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('processDaysBeforeDue') }})
    schedule_dates: Optional[List[ScheduleDate]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scheduleDates') }})
    workflow: Optional[Workflow] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workflow') }})
    


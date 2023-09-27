# PayrollSettings
(*payroll_settings*)

### Available Operations

* [get](#get) - Get payroll settings
* [update](#update) - Update payroll settings

## get

Get payroll settings

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.payroll_settings.get(id='voluptatem')

if res.payroll_settings is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.GetPayrollSettingsResponse](../../models/operations/getpayrollsettingsresponse.md)**


## update

Update payroll settings

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()


res = s.payroll_settings.update(id='cumque', payroll_settings_update=shared.PayrollSettingsUpdate(
    calculation_settings1099=[],
    enable_planned_payroll=[],
    enable_process_days_before_due=[],
    frequency=[],
    funding_source=[],
    issue1099s=[],
    process_days_before_due=7469.94,
    schedule_dates=[
        [],
    ],
    status=shared.StatusPayrollSettingsUpdate.CANCELLED,
    workflow=shared.WorkflowPayrollSettingsUpdate.SINGLE_STAGE,
))

if res.payroll_settings is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `id`                                                                                   | *str*                                                                                  | :heavy_check_mark:                                                                     | Unique identifier                                                                      |
| `payroll_settings_update`                                                              | [Optional[shared.PayrollSettingsUpdate]](../../models/shared/payrollsettingsupdate.md) | :heavy_minus_sign:                                                                     | N/A                                                                                    |


### Response

**[operations.UpdatePayrollSettingsResponse](../../models/operations/updatepayrollsettingsresponse.md)**


# payroll_settings

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


res = s.payroll_settings.get(id='laborum')

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


res = s.payroll_settings.update(id='sed', payroll_settings_update=shared.PayrollSettingsUpdate(
    calculation_settings1099='commodi',
    enable_planned_payroll=False,
    enable_process_days_before_due='voluptas',
    frequency=shared.FrequencyUpdate(
        daily='suscipit',
        day_in_interval=9602.57,
        end_date='debitis',
        every=724.34,
        interval=shared.IntervalFrequencyUpdate.LESS_THAN_NIL_GREATER_THAN_,
        start_date='perferendis',
        twice_per_month=False,
    ),
    funding_source=shared.FundingSource(
        funding_source_currency=shared.FundingSourceCurrency.USD,
        funding_source_id='sed',
        funding_source_type=shared.TypeFundingSource.ACCOUNT,
    ),
    issue1099s='necessitatibus',
    process_days_before_due=2155.29,
    schedule_dates=[
        'occaecati',
    ],
    status=shared.StatusPayrollSettingsUpdate.EXPIRED,
    workflow=shared.WorkflowPayrollSettingsUpdate.LESS_THAN_NIL_GREATER_THAN_,
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


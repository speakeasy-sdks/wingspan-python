# PayrollSettings

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


res = s.payroll_settings.get(id='dolore')

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


res = s.payroll_settings.update(id='aliquam', payroll_settings_update=shared.PayrollSettingsUpdate(
    calculation_settings1099=shared.CalculationSettings1099(
        card_processing_fees=shared.CardProcessingFeesCalculationSettings1099.LESS_THAN_NIL_GREATER_THAN_,
        off_platform_payments=shared.OffPlatformPaymentsCalculationSettings1099.EXCLUDE,
        reimbursable_expenses=shared.ReimbursableExpensesCalculationSettings1099.INCLUDE,
        state_tax_id={
            "blanditiis": 'quas',
        },
        threshold_amount=9425.84,
    ),
    enable_planned_payroll='culpa',
    enable_process_days_before_due=False,
    frequency=shared.FrequencyUpdate(
        daily=False,
        day_in_interval=9402.1,
        end_date='exercitationem',
        every=7507.65,
        interval=shared.IntervalFrequencyUpdate.WEEK,
        start_date='rerum',
        twice_per_month='reiciendis',
    ),
    funding_source='asperiores',
    issue1099s=False,
    process_days_before_due=4518.22,
    schedule_dates=[
        shared.ScheduleDateUpdate(
            date_='ab',
            invoice_template_id='iste',
            status=shared.StatusScheduleDateUpdate.COMPLETED,
        ),
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


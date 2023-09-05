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


res = s.payroll_settings.get(id='fuga')

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


res = s.payroll_settings.update(id='ratione', payroll_settings_update=shared.PayrollSettingsUpdate(
    calculation_settings1099=shared.CalculationSettings1099(
        card_processing_fees=shared.CardProcessingFeesCalculationSettings1099.LESS_THAN_NIL_GREATER_THAN_,
        off_platform_payments=shared.OffPlatformPaymentsCalculationSettings1099.LESS_THAN_NIL_GREATER_THAN_,
        reimbursable_expenses=shared.ReimbursableExpensesCalculationSettings1099.INCLUDE,
        state_tax_id='et',
        threshold_amount=4977.77,
    ),
    enable_planned_payroll=False,
    enable_process_days_before_due=False,
    frequency='adipisci',
    funding_source='magni',
    issue1099s=False,
    process_days_before_due=8595.81,
    schedule_dates=[
        'tempora',
        'molestiae',
        'iusto',
        'praesentium',
    ],
    status=shared.StatusPayrollSettingsUpdate.LESS_THAN_NIL_GREATER_THAN_,
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


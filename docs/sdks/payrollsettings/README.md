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


res = s.payroll_settings.get(id='string')

if res.payroll_settings is not None:
    # handle response
    pass
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


res = s.payroll_settings.update(id='string', payroll_settings_update=shared.PayrollSettingsUpdate(
    calculation_settings1099=shared.CalculationSettings1099(
        state_tax_id={
            "key": 'string',
        },
    ),
    frequency=shared.FrequencyUpdate(),
    funding_source=shared.FundingSource(
        funding_source_currency=shared.FundingSourceCurrency.CAD,
        funding_source_id='string',
        funding_source_type=shared.TypeFundingSource.INTERNAL_ACCOUNT,
    ),
    schedule_dates=[
        shared.ScheduleDateUpdate(),
    ],
))

if res.payroll_settings is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `id`                                                                                   | *str*                                                                                  | :heavy_check_mark:                                                                     | Unique identifier                                                                      |
| `payroll_settings_update`                                                              | [Optional[shared.PayrollSettingsUpdate]](../../models/shared/payrollsettingsupdate.md) | :heavy_minus_sign:                                                                     | N/A                                                                                    |


### Response

**[operations.UpdatePayrollSettingsResponse](../../models/operations/updatepayrollsettingsresponse.md)**


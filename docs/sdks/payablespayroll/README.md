# PayablesPayroll
(*payables_payroll*)

### Available Operations

* [list](#list) - Get a list of payables connected to payroll run

## list

Get a list of payables connected to payroll run

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.payables_payroll.list(payroll_id='Bicycle')

if res.payroll_report_response is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `payroll_id`                                                           | *str*                                                                  | :heavy_check_mark:                                                     | Unique identifier of a invoice with some constraints like invoice type |


### Response

**[operations.ListPayablesPayrollResponse](../../models/operations/listpayablespayrollresponse.md)**


# Payroll
(*payroll*)

### Available Operations

* [execute](#execute) - Execute payroll

## execute

Execute payroll

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.payroll.execute()

if res.invoice is not None:
    # handle response
    pass
```


### Response

**[operations.ExecutePayrollResponse](../../models/operations/executepayrollresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

# ClientDeductions

### Available Operations

* [list](#list) - List deductions

## list

List deductions

### Example Usage

```python
import wingspan


s = wingspan.Wingspan()


res = s.client_deductions.list()

if res.deduction_responses is not None:
    # handle response
```


### Response

**[operations.ListClientDeductionsResponse](../../models/operations/listclientdeductionsresponse.md)**


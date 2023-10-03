# ApprovedPayables
(*approved_payables*)

### Available Operations

* [list](#list) - List approved payables for payroll

## list

List approved payables for payroll

### Example Usage

```python
import wingspan


s = wingspan.Wingspan()


res = s.approved_payables.list()

if res.payable_schemas is not None:
    # handle response
```


### Response

**[operations.ListApprovedPayablesResponse](../../models/operations/listapprovedpayablesresponse.md)**


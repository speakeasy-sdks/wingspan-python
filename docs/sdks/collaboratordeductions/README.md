# CollaboratorDeductions
(*collaborator_deductions*)

### Available Operations

* [list](#list) - List deductions

## list

List deductions

### Example Usage

```python
import wingspan


s = wingspan.Wingspan()


res = s.collaborator_deductions.list()

if res.deduction_responses is not None:
    # handle response
    pass
```


### Response

**[operations.ListCollaboratorDeductionsResponse](../../models/operations/listcollaboratordeductionsresponse.md)**


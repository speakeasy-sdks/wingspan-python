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

if res.classes is not None:
    # handle response
    pass
```


### Response

**[operations.ListCollaboratorDeductionsResponse](../../models/operations/listcollaboratordeductionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

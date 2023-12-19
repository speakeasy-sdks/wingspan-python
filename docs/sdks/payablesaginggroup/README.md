# PayablesAgingGroup
(*payables_aging_group*)

### Available Operations

* [get](#get) - Get a list of payables with respective aging group

## get

Get a list of payables with respective aging group

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.payables_aging_group.get()

if res.classes is not None:
    # handle response
    pass
```


### Response

**[operations.GetPayablesAgingGroupResponse](../../models/operations/getpayablesaginggroupresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

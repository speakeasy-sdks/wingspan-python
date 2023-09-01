# mcc

### Available Operations

* [list](#list) - List mcc codes

## list

List mcc codes

### Example Usage

```python
import wingspan


s = wingspan.Wingspan()


res = s.mcc.list()

if res.mcc_responses is not None:
    # handle response
```


### Response

**[operations.ListMCCResponse](../../models/operations/listmccresponse.md)**


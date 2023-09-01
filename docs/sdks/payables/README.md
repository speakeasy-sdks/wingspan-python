# payables

### Available Operations

* [get](#get) - Get payables summary

## get

Get payables summary

### Example Usage

```python
import petstore


s = petstore.Petstore()


res = s.payables.get()

if res.payables_summary is not None:
    # handle response
```


### Response

**[operations.GetPayablesResponse](../../models/operations/getpayablesresponse.md)**


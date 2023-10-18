# Payables
(*payables*)

### Available Operations

* [get](#get) - Get payables summary

## get

Get payables summary

### Example Usage

```python
import wingspan


s = wingspan.Wingspan()


res = s.payables.get()

if res.payables_summary is not None:
    # handle response
    pass
```


### Response

**[operations.GetPayablesResponse](../../models/operations/getpayablesresponse.md)**


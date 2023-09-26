# ServiceStatus

### Available Operations

* [get](#get) - Get Service Status

## get

Get Service Status

### Example Usage

```python
import wingspan


s = wingspan.Wingspan()


res = s.service_status.get()

if res.ping is not None:
    # handle response
```


### Response

**[operations.GetServiceStatusResponse](../../models/operations/getservicestatusresponse.md)**


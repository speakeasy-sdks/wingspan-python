# service_status

### Available Operations

* [get](#get) - Get Service Status

## get

Get Service Status

### Example Usage

```python
import petstore


s = petstore.Petstore()


res = s.service_status.get()

if res.ping is not None:
    # handle response
```


### Response

**[operations.GetServiceStatusResponse](../../models/operations/getservicestatusresponse.md)**


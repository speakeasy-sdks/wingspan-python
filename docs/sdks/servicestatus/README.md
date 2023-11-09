# ServiceStatus
(*service_status*)

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
    pass
```


### Response

**[operations.GetServiceStatusResponse](../../models/operations/getservicestatusresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

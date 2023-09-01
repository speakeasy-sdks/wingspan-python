# institution

### Available Operations

* [get](#get) - Get Institution By Routing Number

## get

Get Institution By Routing Number

### Example Usage

```python
import petstore
from petstore.models import operations

s = petstore.Petstore()

req = operations.GetInstitutionRequest(
    routing_number='quidem',
)

res = s.institution.get(req)

if res.institution_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetInstitutionRequest](../../models/operations/getinstitutionrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetInstitutionResponse](../../models/operations/getinstitutionresponse.md)**


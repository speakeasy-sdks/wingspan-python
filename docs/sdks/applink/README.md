# app_link

### Available Operations

* [get](#get) - Gets an application link for creating the clearing bank account

## get

Gets an application link for creating the clearing bank account

### Example Usage

```python
import petstore
from petstore.models import operations

s = petstore.Petstore()

req = operations.GetAppLinkRequest(
    member_id='laboriosam',
)

res = s.app_link.get(req)

if res.banking_application_form is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetAppLinkRequest](../../models/operations/getapplinkrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.GetAppLinkResponse](../../models/operations/getapplinkresponse.md)**


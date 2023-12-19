# ClientDeduction
(*client_deduction*)

### Available Operations

* [create](#create) - Create deduction

## create

Create deduction

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()

req = shared.DeductionCreateRequest(
    amount=4865.89,
    client_id='string',
    currency=shared.DeductionCreateRequestCurrency.USD,
    member_id='string',
    name='string',
    type=shared.TypeDeductionCreateRequest.POST_PAYMENT,
)

res = s.client_deduction.create(req)

if res.deduction_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.DeductionCreateRequest](../../models/shared/deductioncreaterequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.CreateClientDeductionResponse](../../models/operations/createclientdeductionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

# client_deduction

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
    amount=5691.01,
    client_id='odit',
    currency=shared.DeductionCreateRequestCurrency.USD,
    member_id='accusantium',
    name='Ebony Predovic',
    priority=4200.75,
    source_invoice_id='nam',
    start_date='eaque',
    type=shared.TypeDeductionCreateRequest.POST_PAYMENT,
)

res = s.client_deduction.create(req)

if res.deduction_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.DeductionCreateRequest](../../models/shared/deductioncreaterequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.CreateClientDeductionResponse](../../models/operations/createclientdeductionresponse.md)**


# ClientDeduction

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
    amount=6974.29,
    client_id='ipsam',
    currency=shared.DeductionCreateRequestCurrency.USD,
    member_id='autem',
    name='Gary Streich',
    priority=166.27,
    source_invoice_id='fugiat',
    start_date='amet',
    type=shared.TypeDeductionCreateRequest.PRE_PAYMENT,
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


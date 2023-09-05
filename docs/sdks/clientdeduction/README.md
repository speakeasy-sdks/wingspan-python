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
    amount=2187.49,
    client_id='hic',
    currency=shared.DeductionCreateRequestCurrency.CAD,
    member_id='cum',
    name='Marian Wisozk',
    priority=2543.56,
    source_invoice_id='veritatis',
    start_date='ipsa',
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


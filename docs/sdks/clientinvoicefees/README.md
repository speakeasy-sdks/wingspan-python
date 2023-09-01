# client_invoice_fees

### Available Operations

* [list](#list) - List client-invoice fees

## list

List client-invoice fees

### Example Usage

```python
import petstore
from petstore.models import operations

s = petstore.Petstore()

req = operations.ListClientInvoiceFeesRequest(
    invoice_id='voluptatibus',
)

res = s.client_invoice_fees.list(req)

if res.invoice_fee_calculation is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.ListClientInvoiceFeesRequest](../../models/operations/listclientinvoicefeesrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.ListClientInvoiceFeesResponse](../../models/operations/listclientinvoicefeesresponse.md)**


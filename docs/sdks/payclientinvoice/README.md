# pay_client_invoice

### Available Operations

* [post](#post) - Pay client-invoice

## post

Pay client-invoice

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()


res = s.pay_client_invoice.post(invoice_id='maiores', pay_request=shared.PayRequest(
    account_id='natus',
    payment_method_id='velit',
    plaid_public_token='voluptatibus',
))

if res.client_invoice is not None:
    # handle response
```

### Parameters

| Parameter                                                        | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `invoice_id`                                                     | *str*                                                            | :heavy_check_mark:                                               | Unique identifier of an invoice                                  |
| `pay_request`                                                    | [Optional[shared.PayRequest]](../../models/shared/payrequest.md) | :heavy_minus_sign:                                               | N/A                                                              |


### Response

**[operations.PostPayClientInvoiceResponse](../../models/operations/postpayclientinvoiceresponse.md)**


# PayClientInvoice
(*pay_client_invoice*)

### Available Operations

* [post](#post) - Pay client-invoice

## post

Pay client-invoice

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()


res = s.pay_client_invoice.post(invoice_id='payment', pay_request=shared.PayRequest())

if res.client_invoice is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                        | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `invoice_id`                                                     | *str*                                                            | :heavy_check_mark:                                               | Unique identifier of an invoice                                  |
| `pay_request`                                                    | [Optional[shared.PayRequest]](../../models/shared/payrequest.md) | :heavy_minus_sign:                                               | N/A                                                              |


### Response

**[operations.PostPayClientInvoiceResponse](../../models/operations/postpayclientinvoiceresponse.md)**


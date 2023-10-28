# ClientInvoice
(*client_invoice*)

### Available Operations

* [get](#get) - Get client-invoice by invoiceId
* [update](#update) - Update client-invoice by invoiceId

## get

Get client-invoice by invoiceId

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.client_invoice.get(id='string')

if res.client_invoice is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.GetClientInvoiceResponse](../../models/operations/getclientinvoiceresponse.md)**


## update

Update client-invoice by invoiceId

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()


res = s.client_invoice.update(id='string', client_invoice_update_request=shared.ClientInvoiceUpdateRequest(
    credit_fee_handling=shared.FeeHandlingConfig(),
))

if res.client_invoice is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `id`                                                                                             | *str*                                                                                            | :heavy_check_mark:                                                                               | Unique identifier                                                                                |
| `client_invoice_update_request`                                                                  | [Optional[shared.ClientInvoiceUpdateRequest]](../../models/shared/clientinvoiceupdaterequest.md) | :heavy_minus_sign:                                                                               | N/A                                                                                              |


### Response

**[operations.UpdateClientInvoiceResponse](../../models/operations/updateclientinvoiceresponse.md)**


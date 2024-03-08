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

s = wingspan.Wingspan()


res = s.client_invoice.get(id='<value>')

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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update

Update client-invoice by invoiceId

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()


res = s.client_invoice.update(id='<value>', client_invoice_update_request=shared.ClientInvoiceUpdateRequest())

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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

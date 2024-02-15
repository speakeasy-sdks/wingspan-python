# ClientInvoiceFees
(*client_invoice_fees*)

### Available Operations

* [create](#create) - Create client-invoice fees
* [list](#list) - List client-invoice fees

## create

Create client-invoice fees

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()

req = shared.TestInvoiceCreate(
    contact_name='<value>',
    email='Jena.Nienow28@yahoo.com',
)

res = s.client_invoice_fees.create(req)

if res.client_invoice is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [shared.TestInvoiceCreate](../../models/shared/testinvoicecreate.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.CreateClientInvoiceFeesResponse](../../models/operations/createclientinvoicefeesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list

List client-invoice fees

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.client_invoice_fees.list(invoice_id='<value>')

if res.invoice_fee_calculation is not None:
    # handle response
    pass
```

### Parameters

| Parameter                       | Type                            | Required                        | Description                     |
| ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| `invoice_id`                    | *str*                           | :heavy_check_mark:              | Unique identifier of an invoice |


### Response

**[operations.ListClientInvoiceFeesResponse](../../models/operations/listclientinvoicefeesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

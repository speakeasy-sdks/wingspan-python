# MemberInvoice
(*member_invoice*)

### Available Operations

* [create](#create) - Create invoice on member
* [delete](#delete) - Delete invoice on member by invoiceId
* [get](#get) - Get invoice on member by invoiceId
* [update](#update) - Update invoice on member by invoiceId

## create

Create invoice on member

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()

req = shared.InvoiceCreateRequest(
    credit_fee_handling=shared.FeeHandlingConfig(),
    due_date='string',
    line_items=[
        shared.InvoiceLineItemsCreateRequest(),
    ],
    member_client_id='string',
)

res = s.member_invoice.create(req)

if res.invoice is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [shared.InvoiceCreateRequest](../../models/shared/invoicecreaterequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.CreateMemberInvoiceResponse](../../models/operations/creatememberinvoiceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete

Delete invoice on member by invoiceId

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.member_invoice.delete(id='string')

if res.invoice is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.DeleteMemberInvoiceResponse](../../models/operations/deletememberinvoiceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get

Get invoice on member by invoiceId

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.member_invoice.get(id='string')

if res.invoice is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.GetMemberInvoiceResponse](../../models/operations/getmemberinvoiceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update

Update invoice on member by invoiceId

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()


res = s.member_invoice.update(id='string', invoice_update_request=shared.InvoiceUpdateRequest())

if res.invoice is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `id`                                                                                 | *str*                                                                                | :heavy_check_mark:                                                                   | Unique identifier                                                                    |
| `invoice_update_request`                                                             | [Optional[shared.InvoiceUpdateRequest]](../../models/shared/invoiceupdaterequest.md) | :heavy_minus_sign:                                                                   | N/A                                                                                  |


### Response

**[operations.UpdateMemberInvoiceResponse](../../models/operations/updatememberinvoiceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

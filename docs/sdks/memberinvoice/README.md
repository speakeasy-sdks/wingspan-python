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
    accepted_payment_methods=[
        shared.InvoiceCreateRequestAcceptedPaymentMethods.CREDIT,
    ],
    attachments=[],
    client=[],
    collaborators=[
        [],
    ],
    credit_fee_handling=shared.FeeHandlingConfig(
        client_absolute_percentage=206.51,
        client_pays=2292.19,
        member_pays=7583.79,
    ),
    currency=shared.CurrencyInvoiceCreateRequest.LESS_THAN_NIL_GREATER_THAN_,
    due_date='ad',
    integration=[],
    invoice_notes='saepe',
    labels=[],
    late_fee_handling=[],
    line_items=[
        shared.InvoiceLineItemsCreateRequest(
            cost_per_unit=3834.64,
            description='deserunt',
            detail='provident',
            discount=[],
            integration=[],
            labels=[],
            quantity=3246.83,
            reimbursable_expense=[],
            total_cost=8310.49,
            unit='totam',
        ),
    ],
    member=[],
    member_client_id='similique',
    metadata=[],
    notification_preferences=[],
    status=shared.StatusInvoiceCreateRequest.DRAFT,
)

res = s.member_invoice.create(req)

if res.invoice is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [shared.InvoiceCreateRequest](../../models/shared/invoicecreaterequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.CreateMemberInvoiceResponse](../../models/operations/creatememberinvoiceresponse.md)**


## delete

Delete invoice on member by invoiceId

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.member_invoice.delete(id='at')

if res.invoice is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.DeleteMemberInvoiceResponse](../../models/operations/deletememberinvoiceresponse.md)**


## get

Get invoice on member by invoiceId

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.member_invoice.get(id='quaerat')

if res.invoice is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.GetMemberInvoiceResponse](../../models/operations/getmemberinvoiceresponse.md)**


## update

Update invoice on member by invoiceId

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()


res = s.member_invoice.update(id='tempora', invoice_update_request=shared.InvoiceUpdateRequest(
    accepted_payment_methods=[
        shared.InvoiceUpdateRequestAcceptedPaymentMethods.ACH,
    ],
    attachments=[],
    charged_fees=[],
    client=[],
    collaborators=[
        [],
    ],
    credit_fee_handling=[],
    due_date='quod',
    integration=[],
    invoice_notes='officiis',
    labels=[],
    late_fee_handling=[],
    line_items=[
        [],
    ],
    member=[],
    member_client_id='qui',
    metadata=[],
    notification_preferences=[],
    status=shared.StatusInvoiceUpdateRequest.PAYMENT_IN_TRANSIT,
))

if res.invoice is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `id`                                                                                 | *str*                                                                                | :heavy_check_mark:                                                                   | Unique identifier                                                                    |
| `invoice_update_request`                                                             | [Optional[shared.InvoiceUpdateRequest]](../../models/shared/invoiceupdaterequest.md) | :heavy_minus_sign:                                                                   | N/A                                                                                  |


### Response

**[operations.UpdateMemberInvoiceResponse](../../models/operations/updatememberinvoiceresponse.md)**


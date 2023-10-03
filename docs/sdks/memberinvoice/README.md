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
        shared.InvoiceCreateRequestAcceptedPaymentMethods.ACH,
    ],
    attachments=[],
    client=[],
    collaborators=[
        [],
    ],
    credit_fee_handling=shared.FeeHandlingConfig(
        client_absolute_percentage=4893.82,
        client_pays=6384.24,
        member_pays=8592.13,
    ),
    currency=shared.CurrencyInvoiceCreateRequest.CAD,
    due_date='South',
    integration=[],
    invoice_notes='grey technology East',
    labels=[],
    late_fee_handling=[],
    line_items=[
        shared.InvoiceLineItemsCreateRequest(
            cost_per_unit=1697.27,
            description='Front-line asynchronous paradigm',
            detail='SUV quantify Polestar',
            discount=[],
            integration=[],
            labels=[],
            quantity=4915.7,
            reimbursable_expense=[],
            total_cost=9574.09,
            unit='becquerel',
        ),
    ],
    member=[],
    member_client_id='Durham after',
    metadata=[],
    notification_preferences=[],
    status=shared.StatusInvoiceCreateRequest.PENDING,
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


res = s.member_invoice.delete(id='program')

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


res = s.member_invoice.get(id='female')

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


res = s.member_invoice.update(id='Van', invoice_update_request=shared.InvoiceUpdateRequest(
    accepted_payment_methods=[
        shared.InvoiceUpdateRequestAcceptedPaymentMethods.CREDIT,
    ],
    attachments=[],
    charged_fees=[],
    client=[],
    collaborators=[
        [],
    ],
    credit_fee_handling=[],
    due_date='male Metal',
    integration=[],
    invoice_notes='Arizona Cotton extend',
    labels=[],
    late_fee_handling=[],
    line_items=[
        [],
    ],
    member=[],
    member_client_id='bifurcated',
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


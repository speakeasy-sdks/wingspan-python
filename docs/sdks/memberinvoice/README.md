# MemberInvoice

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
    attachments='totam',
    client=shared.InvoiceCreateRequestClient2(),
    collaborators=[
        'odio',
    ],
    credit_fee_handling=shared.FeeHandlingConfig(
        client_absolute_percentage=5775.43,
        client_pays=4145.67,
        member_pays=9594.34,
    ),
    currency=shared.CurrencyInvoiceCreateRequest.USD,
    due_date='deserunt',
    integration='accusantium',
    invoice_notes='porro',
    labels='quas',
    late_fee_handling=shared.LateFeeConfigUpdate(
        frequency='deleniti',
        late_fee_amount=1438.29,
        late_fee_percentage=6813.93,
    ),
    line_items=[
        shared.InvoiceLineItemsCreateRequest(
            cost_per_unit=6494.63,
            description='incidunt',
            detail='atque',
            discount='minima',
            integration='fugit',
            labels={
                "consequuntur": 'ratione',
            },
            quantity=1294.12,
            reimbursable_expense=False,
            total_cost=5789.22,
            unit='atque',
        ),
    ],
    member='esse',
    member_client_id='eveniet',
    metadata=shared.InvoiceMetadata(
        purchase_order_number='veritatis',
    ),
    notification_preferences='quod',
    status=shared.StatusInvoiceCreateRequest.PAYMENT_IN_TRANSIT,
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


res = s.member_invoice.delete(id='vero')

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


res = s.member_invoice.get(id='aliquid')

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


res = s.member_invoice.update(id='quasi', invoice_update_request=shared.InvoiceUpdateRequest(
    accepted_payment_methods=[
        shared.InvoiceUpdateRequestAcceptedPaymentMethods.LESS_THAN_NIL_GREATER_THAN_,
    ],
    attachments='harum',
    charged_fees='rerum',
    client=shared.InvoiceUpdateRequestClient2(),
    collaborators=[
        'distinctio',
    ],
    credit_fee_handling=shared.FeeHandlingConfig(
        client_absolute_percentage=270.69,
        client_pays=6360.61,
        member_pays=7313.98,
    ),
    due_date='adipisci',
    integration=shared.ThreeBillionOneHundredAndNinetyMillionSixHundredAndEightyFiveThousandEightHundredAndThirtyTwoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461(
        quickbooks='consequatur',
    ),
    invoice_notes='minus',
    labels='sapiente',
    late_fee_handling='esse',
    line_items=[
        shared.InvoiceLineItemsCreateRequest(
            cost_per_unit=5909.84,
            description='a',
            detail='nulla',
            discount=shared.Facb8048736dba546c4c76242d9f8c7111011a7a7483528f37d80226698a1f2b(
                amount=4572.23,
                description='quasi',
                percentage=9518.75,
            ),
            integration=shared.ThreeBillionOneHundredAndNinetyMillionSixHundredAndEightyFiveThousandEightHundredAndThirtyTwoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461(
                quickbooks=shared.Sixad3f4f624fb518510130e879729b00ed8c237d1cebc5477abf34ac340a6424d(
                    expense_account_id='pariatur',
                    item_id='possimus',
                ),
            ),
            labels='eveniet',
            quantity=9924.3,
            reimbursable_expense=False,
            total_cost=850.01,
            unit='consequuntur',
        ),
    ],
    member='similique',
    member_client_id='culpa',
    metadata='tenetur',
    notification_preferences='earum',
    status=shared.StatusInvoiceUpdateRequest.CANCELLED,
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


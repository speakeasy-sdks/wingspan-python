# member_invoice

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
    attachments=shared.ThirtySixb041d426951ffff76360faf03ef8ae938bed9739e6ad9f51acb982782296a2(
        custom_attachment_ids=[
            'consequuntur',
        ],
    ),
    client='minus',
    collaborators=[
        'sapiente',
    ],
    credit_fee_handling=shared.FeeHandlingConfig(
        client_absolute_percentage=2328.65,
        client_pays=4581.39,
        member_pays=5034.27,
    ),
    currency=shared.CurrencyInvoiceCreateRequest.CAD,
    due_date='a',
    integration=shared.ThreeBillionOneHundredAndNinetyMillionSixHundredAndEightyFiveThousandEightHundredAndThirtyTwoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461(
        quickbooks=shared.Sixad3f4f624fb518510130e879729b00ed8c237d1cebc5477abf34ac340a6424d(
            expense_account_id='esse',
            item_id='quasi',
        ),
    ),
    invoice_notes='a',
    labels={
        "sint": 'pariatur',
    },
    late_fee_handling=shared.LateFeeConfigUpdate(
        frequency='eveniet',
        late_fee_amount=9924.3,
        late_fee_percentage=8155.24,
    ),
    line_items=[
        shared.InvoiceLineItemsCreateRequest(
            cost_per_unit=850.01,
            description='consequuntur',
            detail='quasi',
            discount=shared.Facb8048736dba546c4c76242d9f8c7111011a7a7483528f37d80226698a1f2b(
                amount=6336.08,
                description='aliquid',
                percentage=9492.98,
            ),
            integration='earum',
            labels='in',
            quantity=2586.84,
            reimbursable_expense=False,
            total_cost=8490.39,
            unit='soluta',
        ),
    ],
    member='aliquam',
    member_client_id='sapiente',
    metadata='ullam',
    notification_preferences='ullam',
    status=shared.StatusInvoiceCreateRequest.CANCELLED,
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


res = s.member_invoice.delete(id='aut')

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


res = s.member_invoice.get(id='voluptatum')

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


res = s.member_invoice.update(id='qui', invoice_update_request=shared.InvoiceUpdateRequest(
    accepted_payment_methods=[
        shared.InvoiceUpdateRequestAcceptedPaymentMethods.LESS_THAN_NIL_GREATER_THAN_,
    ],
    attachments='deleniti',
    charged_fees=shared.Fees(
        late_fee=shared.Fee(
            amount=996.15,
            calculated_at='omnis',
        ),
        processing_fee=shared.Fee(
            amount=984.78,
            calculated_at='at',
        ),
    ),
    client='voluptate',
    collaborators=[
        'minima',
    ],
    credit_fee_handling='consectetur',
    due_date='adipisci',
    integration=shared.ThreeBillionOneHundredAndNinetyMillionSixHundredAndEightyFiveThousandEightHundredAndThirtyTwoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461(
        quickbooks=shared.Sixad3f4f624fb518510130e879729b00ed8c237d1cebc5477abf34ac340a6424d(
            expense_account_id='accusantium',
            item_id='rem',
        ),
    ),
    invoice_notes='aut',
    labels={
        "eum": 'mollitia',
    },
    late_fee_handling='corrupti',
    line_items=[
        'voluptatem',
    ],
    member='occaecati',
    member_client_id='numquam',
    metadata=shared.InvoiceMetadata(
        purchase_order_number='explicabo',
    ),
    notification_preferences='aut',
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


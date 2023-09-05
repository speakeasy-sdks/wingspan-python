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
        shared.InvoiceCreateRequestAcceptedPaymentMethods.MANUAL,
        shared.InvoiceCreateRequestAcceptedPaymentMethods.CREDIT,
        shared.InvoiceCreateRequestAcceptedPaymentMethods.LESS_THAN_NIL_GREATER_THAN_,
        shared.InvoiceCreateRequestAcceptedPaymentMethods.MANUAL,
    ],
    attachments='aspernatur',
    client='voluptas',
    collaborators=[
        'nobis',
        shared.InvoiceCollaboratorCreateRequest(
            amount=2378.07,
            currency=shared.CurrencyInvoiceCollaboratorCreateRequest.CAD,
            description='dolores',
            member_client_id='blanditiis',
        ),
    ],
    credit_fee_handling=shared.FeeHandlingConfig(
        client_absolute_percentage=4492.92,
        client_pays=2962.42,
        member_pays=3044.68,
    ),
    currency=shared.CurrencyInvoiceCreateRequest.LESS_THAN_NIL_GREATER_THAN_,
    due_date='temporibus',
    integration='adipisci',
    invoice_notes='cum',
    labels={
        "hic": 'nesciunt',
        "culpa": 'corrupti',
        "pariatur": 'totam',
    },
    late_fee_handling=shared.LateFeeConfigUpdate(
        frequency='nobis',
        late_fee_amount=246.19,
        late_fee_percentage=6995.75,
    ),
    line_items=[
        shared.InvoiceLineItemsCreateRequest(
            cost_per_unit=9679.66,
            description='explicabo',
            detail='asperiores',
            discount=shared.Facb8048736dba546c4c76242d9f8c7111011a7a7483528f37d80226698a1f2b(
                amount=4518.22,
                description='expedita',
                percentage=708.69,
            ),
            integration=shared.ThreeBillionOneHundredAndNinetyMillionSixHundredAndEightyFiveThousandEightHundredAndThirtyTwoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461(
                quickbooks='laborum',
            ),
            labels='in',
            quantity=4174.86,
            reimbursable_expense=False,
            total_cost=1312.89,
            unit='voluptas',
        ),
    ],
    member=shared.InvoiceCreateRequestMember2(),
    member_client_id='architecto',
    metadata='sapiente',
    notification_preferences=shared.InvoiceNotificationPreferences(
        send_invoice='reiciendis',
        send_receipt='corrupti',
        send_reminders=False,
    ),
    status=shared.StatusInvoiceCreateRequest.LESS_THAN_NIL_GREATER_THAN_,
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


res = s.member_invoice.delete(id='incidunt')

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


res = s.member_invoice.get(id='sed')

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


res = s.member_invoice.update(id='provident', invoice_update_request=shared.InvoiceUpdateRequest(
    accepted_payment_methods=[
        shared.InvoiceUpdateRequestAcceptedPaymentMethods.LESS_THAN_NIL_GREATER_THAN_,
        shared.InvoiceUpdateRequestAcceptedPaymentMethods.CREDIT,
    ],
    attachments='occaecati',
    charged_fees=shared.Fees(
        late_fee=shared.Fee(
            amount=2716.53,
            calculated_at='tempora',
        ),
        processing_fee='reiciendis',
    ),
    client='sit',
    collaborators=[
        shared.InvoiceCollaboratorUpdateRequest(
            amount=5058.66,
            description='facilis',
        ),
    ],
    credit_fee_handling='incidunt',
    due_date='ipsam',
    integration=shared.ThreeBillionOneHundredAndNinetyMillionSixHundredAndEightyFiveThousandEightHundredAndThirtyTwoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461(
        quickbooks=shared.Sixad3f4f624fb518510130e879729b00ed8c237d1cebc5477abf34ac340a6424d(
            expense_account_id='sit',
            item_id='nobis',
        ),
    ),
    invoice_notes='error',
    labels='minima',
    late_fee_handling=shared.LateFeeConfigUpdate(
        frequency=shared.FrequencyUpdate(
            daily=False,
            day_in_interval=1685.76,
            end_date='aperiam',
            every=9014.83,
            interval=shared.IntervalFrequencyUpdate.WEEK,
            start_date='veniam',
            twice_per_month='officiis',
        ),
        late_fee_amount=1046.27,
        late_fee_percentage=5124.52,
    ),
    line_items=[
        shared.InvoiceLineItemsCreateRequest(
            cost_per_unit=7400.98,
            description='laboriosam',
            detail='dolorum',
            discount=shared.Facb8048736dba546c4c76242d9f8c7111011a7a7483528f37d80226698a1f2b(
                amount=6223.85,
                description='hic',
                percentage=7105.29,
            ),
            integration=shared.ThreeBillionOneHundredAndNinetyMillionSixHundredAndEightyFiveThousandEightHundredAndThirtyTwoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461(
                quickbooks='dolorum',
            ),
            labels='officia',
            quantity=6762.43,
            reimbursable_expense=False,
            total_cost=8792.35,
            unit='tempora',
        ),
        shared.InvoiceLineItemsCreateRequest(
            cost_per_unit=1482.68,
            description='ut',
            detail='fugiat',
            discount='culpa',
            integration=shared.ThreeBillionOneHundredAndNinetyMillionSixHundredAndEightyFiveThousandEightHundredAndThirtyTwoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461(
                quickbooks='consequatur',
            ),
            labels='ipsam',
            quantity=245.27,
            reimbursable_expense=False,
            total_cost=5580.65,
            unit='repudiandae',
        ),
    ],
    member='et',
    member_client_id='blanditiis',
    metadata='sed',
    notification_preferences='vel',
    status=shared.StatusInvoiceUpdateRequest.OVERDUE,
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


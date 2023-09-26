# PayableOnClient

### Available Operations

* [create](#create) - Create payable on client for member
* [update](#update) - Update payable on client by payableId

## create

Create payable on client for member

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()

req = shared.PayableCreateRequest(
    accepted_payment_methods=[
        shared.PayableCreateRequestAcceptedPaymentMethods.CREDIT,
    ],
    attachments='sapiente',
    client='ullam',
    collaborator_id='reprehenderit',
    credit_fee_handling=shared.FeeHandlingConfig(
        client_absolute_percentage=3567.07,
        client_pays=3917.74,
        member_pays=163.28,
    ),
    currency=shared.CurrencyPayableCreateRequest.CAD,
    due_date='qui',
    integration=shared.ThreeBillionOneHundredAndNinetyMillionSixHundredAndEightyFiveThousandEightHundredAndThirtyTwoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461(
        quickbooks='deleniti',
    ),
    invoice_notes='itaque',
    labels={
        "architecto": 'omnis',
    },
    late_fee_handling=shared.LateFeeConfigUpdate(
        frequency='at',
        late_fee_amount=920.27,
        late_fee_percentage=4541.62,
    ),
    line_items=[
        shared.InvoiceLineItemsCreateRequest(
            cost_per_unit=559.65,
            description='minima',
            detail='veritatis',
            discount='adipisci',
            integration=shared.ThreeBillionOneHundredAndNinetyMillionSixHundredAndEightyFiveThousandEightHundredAndThirtyTwoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461(
                quickbooks=shared.Sixad3f4f624fb518510130e879729b00ed8c237d1cebc5477abf34ac340a6424d(
                    expense_account_id='accusantium',
                    item_id='rem',
                ),
            ),
            labels='laudantium',
            quantity=4287.96,
            reimbursable_expense=False,
            total_cost=680.74,
            unit='corrupti',
        ),
    ],
    member='voluptatem',
    member_client_id='dolor',
    metadata=shared.InvoiceMetadata(
        purchase_order_number='numquam',
    ),
    notification_preferences=shared.InvoiceNotificationPreferences(
        send_invoice='voluptas',
        send_receipt='dignissimos',
        send_reminders=False,
    ),
    status=shared.StatusPayableCreateRequest.DRAFT,
)

res = s.payable_on_client.create(req)

if res.payable_schema is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [shared.PayableCreateRequest](../../models/shared/payablecreaterequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.CreatePayableOnClientResponse](../../models/operations/createpayableonclientresponse.md)**


## update

Update payable on client by payableId

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()


res = s.payable_on_client.update(id='maiores', payable_update_request=shared.PayableUpdateRequest(
    accepted_payment_methods=[
        shared.PayableUpdateRequestAcceptedPaymentMethods.MANUAL,
    ],
    attachments='voluptatibus',
    charged_fees='asperiores',
    client='ea',
    collaborators=[
        'consequuntur',
    ],
    credit_fee_handling=shared.FeeHandlingConfig(
        client_absolute_percentage=6387.62,
        client_pays=8070.23,
        member_pays=4903.05,
    ),
    due_date='officia',
    integration=shared.ThreeBillionOneHundredAndNinetyMillionSixHundredAndEightyFiveThousandEightHundredAndThirtyTwoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461(
        quickbooks='quae',
    ),
    invoice_notes='quaerat',
    labels={
        "quod": 'labore',
    },
    late_fee_handling='adipisci',
    line_items=[
        shared.InvoiceLineItemsCreateRequest(
            cost_per_unit=6625.05,
            description='suscipit',
            detail='velit',
            discount=shared.Facb8048736dba546c4c76242d9f8c7111011a7a7483528f37d80226698a1f2b(
                amount=6658.59,
                description='recusandae',
                percentage=5173.09,
            ),
            integration=shared.ThreeBillionOneHundredAndNinetyMillionSixHundredAndEightyFiveThousandEightHundredAndThirtyTwoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461(
                quickbooks='ducimus',
            ),
            labels={
                "vel": 'labore',
            },
            quantity=8225.6,
            reimbursable_expense=False,
            total_cost=7382.27,
            unit='commodi',
        ),
    ],
    member='corporis',
    member_client_id='reiciendis',
    metadata=shared.InvoiceMetadata(
        purchase_order_number='nemo',
    ),
    notification_preferences=shared.InvoiceNotificationPreferences(
        send_invoice='aperiam',
        send_receipt=False,
        send_reminders=False,
    ),
    payment_methods=[
        shared.PayableUpdateRequestPaymentMethods.CREDIT,
    ],
    status=shared.StatusPayableUpdateRequest.CANCELLED,
))

if res.payable_schema is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `id`                                                                                 | *str*                                                                                | :heavy_check_mark:                                                                   | Unique identifier                                                                    |
| `payable_update_request`                                                             | [Optional[shared.PayableUpdateRequest]](../../models/shared/payableupdaterequest.md) | :heavy_minus_sign:                                                                   | N/A                                                                                  |


### Response

**[operations.UpdatePayableOnClientResponse](../../models/operations/updatepayableonclientresponse.md)**


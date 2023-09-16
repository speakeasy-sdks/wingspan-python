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
        shared.PayableCreateRequestAcceptedPaymentMethods.ACH,
    ],
    attachments=shared.ThirtySixb041d426951ffff76360faf03ef8ae938bed9739e6ad9f51acb982782296a2(
        custom_attachment_ids=[
            'aperiam',
        ],
    ),
    client='quaerat',
    collaborator_id='consequuntur',
    credit_fee_handling=shared.FeeHandlingConfig(
        client_absolute_percentage=8315.2,
        client_pays=6387.62,
        member_pays=8070.23,
    ),
    currency=shared.CurrencyPayableCreateRequest.CAD,
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
            cost_per_unit=6835.73,
            description='id',
            detail='suscipit',
            discount='culpa',
            integration=shared.ThreeBillionOneHundredAndNinetyMillionSixHundredAndEightyFiveThousandEightHundredAndThirtyTwoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461(
                quickbooks=shared.Sixad3f4f624fb518510130e879729b00ed8c237d1cebc5477abf34ac340a6424d(
                    expense_account_id='totam',
                    item_id='fugiat',
                ),
            ),
            labels='ducimus',
            quantity=5546.88,
            reimbursable_expense='labore',
            total_cost=8225.6,
            unit='facilis',
        ),
    ],
    member=shared.PayableCreateRequestMember2(),
    member_client_id='commodi',
    metadata='corporis',
    notification_preferences=shared.InvoiceNotificationPreferences(
        send_invoice=False,
        send_receipt='recusandae',
        send_reminders=False,
    ),
    status=shared.StatusPayableCreateRequest.CANCELLED,
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


res = s.payable_on_client.update(id='aperiam', payable_update_request=shared.PayableUpdateRequest(
    accepted_payment_methods=[
        shared.PayableUpdateRequestAcceptedPaymentMethods.MANUAL,
    ],
    attachments='in',
    charged_fees='earum',
    client=shared.PayableUpdateRequestClient2(),
    collaborators=[
        'doloribus',
    ],
    credit_fee_handling='reiciendis',
    due_date='quidem',
    integration=shared.ThreeBillionOneHundredAndNinetyMillionSixHundredAndEightyFiveThousandEightHundredAndThirtyTwoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461(
        quickbooks=shared.Sixad3f4f624fb518510130e879729b00ed8c237d1cebc5477abf34ac340a6424d(
            expense_account_id='dolore',
            item_id='sunt',
        ),
    ),
    invoice_notes='asperiores',
    labels='non',
    late_fee_handling='beatae',
    line_items=[
        'a',
    ],
    member=shared.PayableUpdateRequestMember2(),
    member_client_id='consectetur',
    metadata='harum',
    notification_preferences='ipsa',
    payment_methods=[
        shared.PayableUpdateRequestPaymentMethods.LESS_THAN_NIL_GREATER_THAN_,
    ],
    status=shared.StatusPayableUpdateRequest.PAYMENT_IN_TRANSIT,
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


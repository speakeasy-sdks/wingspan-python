# payable_on_client

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
        shared.PayableCreateRequestAcceptedPaymentMethods.MANUAL,
    ],
    attachments='architecto',
    client=shared.PayableCreateRequestClient2(),
    collaborator_id='labore',
    credit_fee_handling=shared.FeeHandlingConfig(
        client_absolute_percentage=6952.7,
        client_pays=5390.74,
        member_pays=6719.57,
    ),
    currency=shared.CurrencyPayableCreateRequest.LESS_THAN_NIL_GREATER_THAN_,
    due_date='tenetur',
    integration='alias',
    invoice_notes='amet',
    labels={
        "unde": 'reiciendis',
        "provident": 'repellendus',
    },
    late_fee_handling=shared.LateFeeConfigUpdate(
        frequency=shared.FrequencyUpdate(
            daily='est',
            day_in_interval=6964.83,
            end_date='reprehenderit',
            every=8136.79,
            interval=shared.IntervalFrequencyUpdate.LESS_THAN_NIL_GREATER_THAN_,
            start_date='praesentium',
            twice_per_month=False,
        ),
        late_fee_amount=3339.65,
        late_fee_percentage=291,
    ),
    line_items=[
        shared.InvoiceLineItemsCreateRequest(
            cost_per_unit=9195.32,
            description='quasi',
            detail='atque',
            discount='asperiores',
            integration=shared.ThreeBillionOneHundredAndNinetyMillionSixHundredAndEightyFiveThousandEightHundredAndThirtyTwoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461(
                quickbooks='quidem',
            ),
            labels={
                "esse": 'amet',
            },
            quantity=8268.25,
            reimbursable_expense='atque',
            total_cost=6232.95,
            unit='officiis',
        ),
        shared.InvoiceLineItemsCreateRequest(
            cost_per_unit=8869.61,
            description='accusamus',
            detail='natus',
            discount='aspernatur',
            integration='maiores',
            labels={
                "error": 'blanditiis',
                "suscipit": 'repudiandae',
                "atque": 'atque',
                "sunt": 'recusandae',
            },
            quantity=6806.97,
            reimbursable_expense=False,
            total_cost=2871.19,
            unit='reiciendis',
        ),
        shared.InvoiceLineItemsCreateRequest(
            cost_per_unit=429.76,
            description='repudiandae',
            detail='dicta',
            discount='beatae',
            integration='enim',
            labels='velit',
            quantity=9521.43,
            reimbursable_expense=False,
            total_cost=3000.29,
            unit='saepe',
        ),
        shared.InvoiceLineItemsCreateRequest(
            cost_per_unit=1604.67,
            description='occaecati',
            detail='officiis',
            discount=shared.Facb8048736dba546c4c76242d9f8c7111011a7a7483528f37d80226698a1f2b(
                amount=4463.94,
                description='adipisci',
                percentage=9078.76,
            ),
            integration=shared.ThreeBillionOneHundredAndNinetyMillionSixHundredAndEightyFiveThousandEightHundredAndThirtyTwoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461(
                quickbooks='fugit',
            ),
            labels={
                "reprehenderit": 'error',
                "illo": 'corporis',
            },
            quantity=6964.63,
            reimbursable_expense=False,
            total_cost=2473.99,
            unit='vero',
        ),
    ],
    member='iure',
    member_client_id='ipsa',
    metadata=shared.InvoiceMetadata(
        purchase_order_number='quae',
    ),
    notification_preferences='eveniet',
    status=shared.StatusPayableCreateRequest.OPEN,
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


res = s.payable_on_client.update(id='cum', payable_update_request=shared.PayableUpdateRequest(
    accepted_payment_methods=[
        shared.PayableUpdateRequestAcceptedPaymentMethods.LESS_THAN_NIL_GREATER_THAN_,
        shared.PayableUpdateRequestAcceptedPaymentMethods.CREDIT,
    ],
    attachments=shared.ThirtySixb041d426951ffff76360faf03ef8ae938bed9739e6ad9f51acb982782296a2(
        custom_attachment_ids=[
            'voluptatum',
            'rem',
            'aliquam',
        ],
    ),
    charged_fees='repellat',
    client='corporis',
    collaborators=[
        'mollitia',
        'alias',
        shared.InvoiceCollaboratorUpdateRequest(
            amount=9702.22,
            description='dolores',
        ),
    ],
    credit_fee_handling=shared.FeeHandlingConfig(
        client_absolute_percentage=3279.88,
        client_pays=2931.44,
        member_pays=6803.49,
    ),
    due_date='nesciunt',
    integration='recusandae',
    invoice_notes='omnis',
    labels='molestiae',
    late_fee_handling='ut',
    line_items=[
        'debitis',
        shared.InvoiceLineItemsCreateRequest(
            cost_per_unit=4326.06,
            description='nemo',
            detail='recusandae',
            discount='provident',
            integration='eum',
            labels={
                "aspernatur": 'ullam',
                "quasi": 'animi',
                "nostrum": 'mollitia',
            },
            quantity=5910.27,
            reimbursable_expense=False,
            total_cost=6591.77,
            unit='ex',
        ),
        'accusantium',
    ],
    member=shared.PayableUpdateRequestMember2(),
    member_client_id='doloribus',
    metadata='in',
    notification_preferences=shared.InvoiceNotificationPreferences(
        send_invoice=False,
        send_receipt=False,
        send_reminders=False,
    ),
    payment_methods=[
        shared.PayableUpdateRequestPaymentMethods.LESS_THAN_NIL_GREATER_THAN_,
        shared.PayableUpdateRequestPaymentMethods.ACH,
        shared.PayableUpdateRequestPaymentMethods.LESS_THAN_NIL_GREATER_THAN_,
    ],
    status=shared.StatusPayableUpdateRequest.PENDING,
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


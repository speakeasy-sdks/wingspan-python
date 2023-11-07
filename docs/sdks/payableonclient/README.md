# PayableOnClient
(*.payable_on_client*)

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
            'string',
        ],
    ),
    client=shared.PayableCreateRequestClient(),
    collaborator_id='string',
    credit_fee_handling=shared.FeeHandlingConfig(),
    due_date='string',
    integration=shared.ThreeBillionOneHundredAndNinetyMillionSixHundredAndEightyFiveThousandEightHundredAndThirtyTwoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461(
        quickbooks=shared.Sixad3f4f624fb518510130e879729b00ed8c237d1cebc5477abf34ac340a6424d(),
    ),
    labels={
        "key": 'string',
    },
    late_fee_handling=shared.LateFeeConfigUpdate(
        frequency=shared.FrequencyUpdate(),
    ),
    line_items=[
        shared.InvoiceLineItemsCreateRequest(
            discount=shared.Facb8048736dba546c4c76242d9f8c7111011a7a7483528f37d80226698a1f2b(),
            integration=shared.ThreeBillionOneHundredAndNinetyMillionSixHundredAndEightyFiveThousandEightHundredAndThirtyTwoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461(
                quickbooks=shared.Sixad3f4f624fb518510130e879729b00ed8c237d1cebc5477abf34ac340a6424d(),
            ),
            labels={
                "key": 'string',
            },
        ),
    ],
    member=shared.PayableCreateRequestMember(),
    metadata=shared.InvoiceMetadata(),
    notification_preferences=shared.InvoiceNotificationPreferences(
        send_reminders=False,
    ),
)

res = s.payable_on_client.create(req)

if res.payable_schema is not None:
    # handle response
    pass
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


res = s.payable_on_client.update(id='string', payable_update_request=shared.PayableUpdateRequest(
    accepted_payment_methods=[
        shared.PayableUpdateRequestAcceptedPaymentMethods.LESS_THAN_NIL_GREATER_THAN_,
    ],
    attachments=shared.ThirtySixb041d426951ffff76360faf03ef8ae938bed9739e6ad9f51acb982782296a2(
        custom_attachment_ids=[
            'string',
        ],
    ),
    charged_fees=shared.Fees(
        late_fee=shared.Fee(
            amount=245.55,
        ),
        processing_fee=shared.Fee(
            amount=5971.29,
        ),
    ),
    client=shared.PayableUpdateRequestClient(),
    collaborators=[
        shared.InvoiceCollaboratorUpdateRequest(),
    ],
    credit_fee_handling=shared.FeeHandlingConfig(),
    integration=shared.ThreeBillionOneHundredAndNinetyMillionSixHundredAndEightyFiveThousandEightHundredAndThirtyTwoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461(
        quickbooks=shared.Sixad3f4f624fb518510130e879729b00ed8c237d1cebc5477abf34ac340a6424d(),
    ),
    labels={
        "key": 'string',
    },
    late_fee_handling=shared.LateFeeConfigUpdate(
        frequency=shared.FrequencyUpdate(),
    ),
    line_items=[
        shared.InvoiceLineItemsCreateRequest(
            discount=shared.Facb8048736dba546c4c76242d9f8c7111011a7a7483528f37d80226698a1f2b(),
            integration=shared.ThreeBillionOneHundredAndNinetyMillionSixHundredAndEightyFiveThousandEightHundredAndThirtyTwoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461(
                quickbooks=shared.Sixad3f4f624fb518510130e879729b00ed8c237d1cebc5477abf34ac340a6424d(),
            ),
            labels={
                "key": 'string',
            },
        ),
    ],
    member=shared.PayableUpdateRequestMember(),
    metadata=shared.InvoiceMetadata(),
    notification_preferences=shared.InvoiceNotificationPreferences(
        send_reminders=False,
    ),
    payment_methods=[
        shared.PaymentMethods.CREDIT,
    ],
))

if res.payable_schema is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `id`                                                                                 | *str*                                                                                | :heavy_check_mark:                                                                   | Unique identifier                                                                    |
| `payable_update_request`                                                             | [Optional[shared.PayableUpdateRequest]](../../models/shared/payableupdaterequest.md) | :heavy_minus_sign:                                                                   | N/A                                                                                  |


### Response

**[operations.UpdatePayableOnClientResponse](../../models/operations/updatepayableonclientresponse.md)**


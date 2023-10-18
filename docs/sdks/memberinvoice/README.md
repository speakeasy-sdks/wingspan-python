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
    attachments=shared.ThirtySixb041d426951ffff76360faf03ef8ae938bed9739e6ad9f51acb982782296a2(
        custom_attachment_ids=[
            'bluetooth',
        ],
    ),
    client=shared.InvoiceCreateRequestClient(),
    collaborators=[
        shared.InvoiceCollaboratorCreateRequest(
            amount=8592.13,
            currency=shared.CurrencyInvoiceCollaboratorCreateRequest.USD,
            description='Face to face bi-directional productivity',
            member_client_id='Cambridgeshire',
        ),
    ],
    credit_fee_handling=shared.FeeHandlingConfig(),
    due_date='grey',
    integration=shared.ThreeBillionOneHundredAndNinetyMillionSixHundredAndEightyFiveThousandEightHundredAndThirtyTwoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461(
        quickbooks=shared.Sixad3f4f624fb518510130e879729b00ed8c237d1cebc5477abf34ac340a6424d(),
    ),
    labels={
        "technology": 'East',
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
                "orange": 'Northwest',
            },
        ),
    ],
    member=shared.InvoiceCreateRequestMember(),
    member_client_id='fuchsia',
    metadata=shared.InvoiceMetadata(),
    notification_preferences=shared.InvoiceNotificationPreferences(
        send_reminders=False,
    ),
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
    pass
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
    pass
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
    attachments=shared.ThirtySixb041d426951ffff76360faf03ef8ae938bed9739e6ad9f51acb982782296a2(
        custom_attachment_ids=[
            'Reactive',
        ],
    ),
    charged_fees=shared.Fees(
        late_fee=shared.Fee(
            amount=9914.64,
        ),
        processing_fee=shared.Fee(
            amount=2703.24,
        ),
    ),
    client=shared.InvoiceUpdateRequestClient(),
    collaborators=[
        shared.InvoiceCollaboratorUpdateRequest(),
    ],
    credit_fee_handling=shared.FeeHandlingConfig(),
    integration=shared.ThreeBillionOneHundredAndNinetyMillionSixHundredAndEightyFiveThousandEightHundredAndThirtyTwoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461(
        quickbooks=shared.Sixad3f4f624fb518510130e879729b00ed8c237d1cebc5477abf34ac340a6424d(),
    ),
    labels={
        "Quality": 'redundant',
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
                "cheater": 'Islands',
            },
        ),
    ],
    member=shared.InvoiceUpdateRequestMember(),
    metadata=shared.InvoiceMetadata(),
    notification_preferences=shared.InvoiceNotificationPreferences(
        send_reminders=False,
    ),
))

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


# InvoiceTemplate
(*invoice_template*)

### Available Operations

* [create](#create) - Create invoice-template
* [delete](#delete) - Delete invoice-template
* [get](#get) - Get invoice-template
* [update](#update) - Update invoice-template

## create

Create invoice-template

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()

req = shared.InvoiceTemplateCreateRequest(
    invoice_data=shared.InvoiceDataCreateRequest(
        line_items=[
            shared.InvoiceLineItemsCreateRequest(
                discount=shared.Facb8048736dba546c4c76242d9f8c7111011a7a7483528f37d80226698a1f2b(),
                integration=shared.ThreeBillionOneHundredAndNinetyMillionSixHundredAndEightyFiveThousandEightHundredAndThirtyTwoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461(
                    quickbooks=shared.Sixad3f4f624fb518510130e879729b00ed8c237d1cebc5477abf34ac340a6424d(),
                ),
                labels={
                    'key': 'string',
                },
            ),
        ],
        member_client_id='string',
        accepted_payment_methods=[
            shared.InvoiceDataCreateRequestAcceptedPaymentMethods.ACH,
        ],
        attachments=shared.ThirtySixb041d426951ffff76360faf03ef8ae938bed9739e6ad9f51acb982782296a2(
            custom_attachment_ids=[
                'string',
            ],
        ),
        collaborators=[
            shared.InvoiceCollaboratorCreateRequest(
                amount=4893.82,
                currency=shared.CurrencyInvoiceCollaboratorCreateRequest.CAD,
                description='Synchronised full-range emulation',
                member_client_id='string',
            ),
        ],
        credit_fee_handling=shared.FeeHandlingConfig(),
        labels={
            'key': 'string',
        },
        late_fee_handling=shared.LateFeeConfig(
            frequency=shared.Frequency(
                start_date='string',
            ),
        ),
        notification_preferences=shared.InvoiceNotificationPreferences(
            send_reminders=False,
        ),
    ),
    status=shared.StatusInvoiceTemplateCreateRequest.ACTIVE,
    frequency=shared.Frequency(
        start_date='string',
    ),
    labels={
        'key': 'string',
    },
    schedule_dates=[
        shared.ScheduleDate(
            date_='string',
            status=shared.StatusScheduleDate.MODIFIED,
        ),
    ],
)

res = s.invoice_template.create(req)

if res.invoice_template is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [shared.InvoiceTemplateCreateRequest](../../models/shared/invoicetemplatecreaterequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.CreateInvoiceTemplateResponse](../../models/operations/createinvoicetemplateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete

Delete invoice-template

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.invoice_template.delete(id='string')

if res.invoice_template is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.DeleteInvoiceTemplateResponse](../../models/operations/deleteinvoicetemplateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get

Get invoice-template

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.invoice_template.get(id='string')

if res.invoice_template is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.GetInvoiceTemplateResponse](../../models/operations/getinvoicetemplateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update

Update invoice-template

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()


res = s.invoice_template.update(id='string', invoice_template_update_request=shared.InvoiceTemplateUpdateRequest(
    frequency=shared.FrequencyUpdate(),
    invoice_data=shared.InvoiceUpdateRequest(
        accepted_payment_methods=[
            shared.InvoiceUpdateRequestAcceptedPaymentMethods.LESS_THAN_NIL_GREATER_THAN_,
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
        client=shared.InvoiceUpdateRequestClient(),
        collaborators=[
            shared.InvoiceCollaboratorUpdateRequest(),
        ],
        credit_fee_handling=shared.FeeHandlingConfig(),
        integration=shared.ThreeBillionOneHundredAndNinetyMillionSixHundredAndEightyFiveThousandEightHundredAndThirtyTwoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461(
            quickbooks=shared.Sixad3f4f624fb518510130e879729b00ed8c237d1cebc5477abf34ac340a6424d(),
        ),
        labels={
            'key': 'string',
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
                    'key': 'string',
                },
            ),
        ],
        member=shared.InvoiceUpdateRequestMember(),
        metadata=shared.InvoiceMetadata(),
        notification_preferences=shared.InvoiceNotificationPreferences(
            send_reminders=False,
        ),
    ),
    labels={
        'key': 'string',
    },
    schedule_dates=[
        shared.ScheduleDateUpdate(),
    ],
))

if res.invoice_template is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `id`                                                                                                 | *str*                                                                                                | :heavy_check_mark:                                                                                   | Unique identifier                                                                                    |
| `invoice_template_update_request`                                                                    | [Optional[shared.InvoiceTemplateUpdateRequest]](../../models/shared/invoicetemplateupdaterequest.md) | :heavy_minus_sign:                                                                                   | N/A                                                                                                  |


### Response

**[operations.UpdateInvoiceTemplateResponse](../../models/operations/updateinvoicetemplateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

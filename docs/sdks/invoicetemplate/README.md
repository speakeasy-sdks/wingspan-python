# InvoiceTemplate

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
    due_in_days=8623.1,
    frequency='porro',
    invoice_data=shared.InvoiceDataCreateRequest(
        accepted_payment_methods=[
            shared.InvoiceDataCreateRequestAcceptedPaymentMethods.LESS_THAN_NIL_GREATER_THAN_,
        ],
        attachments=shared.ThirtySixb041d426951ffff76360faf03ef8ae938bed9739e6ad9f51acb982782296a2(
            custom_attachment_ids=[
                'iusto',
            ],
        ),
        collaborators=[
            shared.InvoiceCollaboratorCreateRequest(
                amount=4973.91,
                currency=shared.CurrencyInvoiceCollaboratorCreateRequest.USD,
                description='officia',
                member_client_id='tempora',
            ),
        ],
        credit_fee_handling='ea',
        currency=shared.CurrencyInvoiceDataCreateRequest.USD,
        due_date='vel',
        invoice_notes='possimus',
        labels='ratione',
        late_fee_handling='laudantium',
        line_items=[
            shared.InvoiceLineItemsCreateRequest(
                cost_per_unit=1206.57,
                description='dolor',
                detail='maiores',
                discount='ex',
                integration=shared.ThreeBillionOneHundredAndNinetyMillionSixHundredAndEightyFiveThousandEightHundredAndThirtyTwoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461(
                    quickbooks=shared.Sixad3f4f624fb518510130e879729b00ed8c237d1cebc5477abf34ac340a6424d(
                        expense_account_id='voluptatibus',
                        item_id='nostrum',
                    ),
                ),
                labels={
                    "quisquam": 'saepe',
                },
                quantity=4113.72,
                reimbursable_expense=False,
                total_cost=3592.71,
                unit='veniam',
            ),
        ],
        member_client_id='aliquid',
        notification_preferences='magnam',
        status=shared.StatusInvoiceDataCreateRequest.CANCELLED,
    ),
    is_scheduling_only=False,
    labels='recusandae',
    schedule_dates=[
        'minima',
    ],
    send_emails='a',
    status=shared.StatusInvoiceTemplateCreateRequest.EXPIRED,
)

res = s.invoice_template.create(req)

if res.invoice_template is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [shared.InvoiceTemplateCreateRequest](../../models/shared/invoicetemplatecreaterequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.CreateInvoiceTemplateResponse](../../models/operations/createinvoicetemplateresponse.md)**


## delete

Delete invoice-template

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.invoice_template.delete(id='aut')

if res.invoice_template is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.DeleteInvoiceTemplateResponse](../../models/operations/deleteinvoicetemplateresponse.md)**


## get

Get invoice-template

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.invoice_template.get(id='aut')

if res.invoice_template is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.GetInvoiceTemplateResponse](../../models/operations/getinvoicetemplateresponse.md)**


## update

Update invoice-template

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()


res = s.invoice_template.update(id='deleniti', invoice_template_update_request=shared.InvoiceTemplateUpdateRequest(
    account_id='impedit',
    auto_payment_required='fugit',
    due_in_days=8828.6,
    frequency='non',
    invoice_data='dolorum',
    is_scheduling_only=False,
    labels={
        "velit": 'eum',
    },
    payment_method_id='autem',
    schedule_dates=[
        shared.ScheduleDateUpdate(
            date_='quas',
            invoice_template_id='assumenda',
            status=shared.StatusScheduleDateUpdate.LESS_THAN_NIL_GREATER_THAN_,
        ),
    ],
    send_emails='libero',
    status=shared.StatusInvoiceTemplateUpdateRequest.ACTIVE,
))

if res.invoice_template is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `id`                                                                                                 | *str*                                                                                                | :heavy_check_mark:                                                                                   | Unique identifier                                                                                    |
| `invoice_template_update_request`                                                                    | [Optional[shared.InvoiceTemplateUpdateRequest]](../../models/shared/invoicetemplateupdaterequest.md) | :heavy_minus_sign:                                                                                   | N/A                                                                                                  |


### Response

**[operations.UpdateInvoiceTemplateResponse](../../models/operations/updateinvoicetemplateresponse.md)**


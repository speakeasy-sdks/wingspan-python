# invoice_template

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
    due_in_days=5361.78,
    frequency='fuga',
    invoice_data=shared.InvoiceDataCreateRequest(
        accepted_payment_methods=[
            shared.InvoiceDataCreateRequestAcceptedPaymentMethods.ACH,
            shared.InvoiceDataCreateRequestAcceptedPaymentMethods.MANUAL,
            shared.InvoiceDataCreateRequestAcceptedPaymentMethods.CREDIT,
        ],
        attachments='nisi',
        collaborators=[
            shared.InvoiceCollaboratorCreateRequest(
                amount=1598.7,
                currency=shared.CurrencyInvoiceCollaboratorCreateRequest.USD,
                description='explicabo',
                member_client_id='saepe',
            ),
        ],
        credit_fee_handling=shared.FeeHandlingConfig(
            client_absolute_percentage=5438.06,
            client_pays=922.6,
            member_pays=4569.11,
        ),
        currency=shared.CurrencyInvoiceDataCreateRequest.LESS_THAN_NIL_GREATER_THAN_,
        due_date='accusamus',
        invoice_notes='veritatis',
        labels='quod',
        late_fee_handling=shared.LateFeeConfig(
            frequency=shared.Frequency(
                daily=False,
                day_in_interval=3990.25,
                end_date='quasi',
                every=9040.45,
                interval=shared.IntervalFrequency.MONTH,
                start_date='harum',
                twice_per_month='rerum',
            ),
            late_fee_amount=5801.97,
            late_fee_percentage=3277.2,
        ),
        line_items=[
            shared.InvoiceLineItemsCreateRequest(
                cost_per_unit=7567.79,
                description='sit',
                detail='culpa',
                discount=shared.Facb8048736dba546c4c76242d9f8c7111011a7a7483528f37d80226698a1f2b(
                    amount=2400.2,
                    description='cumque',
                    percentage=1605.38,
                ),
                integration='minus',
                labels='sapiente',
                quantity=2328.65,
                reimbursable_expense='blanditiis',
                total_cost=5909.84,
                unit='a',
            ),
            shared.InvoiceLineItemsCreateRequest(
                cost_per_unit=8577.23,
                description='quas',
                detail='esse',
                discount='a',
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
            shared.InvoiceLineItemsCreateRequest(
                cost_per_unit=944.58,
                description='similique',
                detail='culpa',
                discount='tenetur',
                integration='earum',
                labels='in',
                quantity=2586.84,
                reimbursable_expense=False,
                total_cost=8490.39,
                unit='soluta',
            ),
        ],
        member_client_id='accusantium',
        notification_preferences='sapiente',
        status=shared.StatusInvoiceDataCreateRequest.DRAFT,
    ),
    is_scheduling_only='reprehenderit',
    labels='nisi',
    schedule_dates=[
        shared.ScheduleDate(
            cut_off_date='qui',
            date_='quibusdam',
            invoice_id='ex',
            invoice_template_id='deleniti',
            status=shared.StatusScheduleDate.MODIFIED,
        ),
    ],
    send_emails=False,
    status=shared.StatusInvoiceTemplateCreateRequest.ACTIVE,
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


res = s.invoice_template.delete(id='omnis')

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


res = s.invoice_template.get(id='tenetur')

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


res = s.invoice_template.update(id='quasi', invoice_template_update_request=shared.InvoiceTemplateUpdateRequest(
    account_id='at',
    auto_payment_required='voluptate',
    due_in_days=559.65,
    frequency='veritatis',
    invoice_data='adipisci',
    is_scheduling_only=False,
    labels={
        "rem": 'aut',
    },
    payment_method_id='laudantium',
    schedule_dates=[
        shared.ScheduleDateUpdate(
            date_='ab',
            invoice_template_id='corrupti',
            status=shared.StatusScheduleDateUpdate.COMPLETED,
        ),
        'dolor',
    ],
    send_emails=False,
    status=shared.StatusInvoiceTemplateUpdateRequest.DRAFT,
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


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
    due_in_days=4856.28,
    frequency=shared.Frequency(
        daily=False,
        day_in_interval=7875.42,
        end_date='vero',
        every=6064.76,
        interval=shared.IntervalFrequency.MONTH,
        start_date='ipsum',
        twice_per_month=False,
    ),
    invoice_data=shared.InvoiceDataCreateRequest(
        accepted_payment_methods=[
            shared.InvoiceDataCreateRequestAcceptedPaymentMethods.ACH,
        ],
        attachments='vero',
        collaborators=[
            shared.InvoiceCollaboratorCreateRequest(
                amount=4922.68,
                currency=shared.CurrencyInvoiceCollaboratorCreateRequest.CAD,
                description='distinctio',
                member_client_id='quod',
            ),
        ],
        credit_fee_handling='similique',
        currency=shared.CurrencyInvoiceDataCreateRequest.LESS_THAN_NIL_GREATER_THAN_,
        due_date='vero',
        invoice_notes='ducimus',
        labels='quibusdam',
        late_fee_handling=shared.LateFeeConfig(
            frequency=shared.Frequency(
                daily='natus',
                day_in_interval=7733.26,
                end_date='aut',
                every=9742.59,
                interval=shared.IntervalFrequency.MONTH,
                start_date='nulla',
                twice_per_month='porro',
            ),
            late_fee_amount=9818.3,
            late_fee_percentage=9850.33,
        ),
        line_items=[
            shared.InvoiceLineItemsCreateRequest(
                cost_per_unit=4783.7,
                description='eligendi',
                detail='ducimus',
                discount='officia',
                integration='ipsam',
                labels='aspernatur',
                quantity=4282.24,
                reimbursable_expense=False,
                total_cost=2978.42,
                unit='ratione',
            ),
        ],
        member_client_id='ex',
        notification_preferences=shared.InvoiceNotificationPreferences(
            send_invoice='dolor',
            send_receipt=False,
            send_reminders=False,
        ),
        status=shared.StatusInvoiceDataCreateRequest.DRAFT,
    ),
    is_scheduling_only='nulla',
    labels={
        "voluptatibus": 'nostrum',
    },
    schedule_dates=[
        shared.ScheduleDate(
            cut_off_date='quisquam',
            date_='saepe',
            invoice_id='ea',
            invoice_template_id='impedit',
            status=shared.StatusScheduleDate.COMPLETED,
        ),
    ],
    send_emails='aliquid',
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


res = s.invoice_template.delete(id='magnam')

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


res = s.invoice_template.get(id='ea')

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


res = s.invoice_template.update(id='quo', invoice_template_update_request=shared.InvoiceTemplateUpdateRequest(
    account_id='consectetur',
    auto_payment_required=False,
    due_in_days=1324.87,
    frequency='eaque',
    invoice_data=shared.InvoiceUpdateRequest(
        accepted_payment_methods=[
            shared.InvoiceUpdateRequestAcceptedPaymentMethods.MANUAL,
        ],
        attachments='aut',
        charged_fees=shared.Fees(
            late_fee=shared.Fee(
                amount=3045.82,
                calculated_at='fugit',
            ),
            processing_fee=shared.Fee(
                amount=795.22,
                calculated_at='non',
            ),
        ),
        client='dolorum',
        collaborators=[
            shared.InvoiceCollaboratorUpdateRequest(
                amount=8104.24,
                description='velit',
            ),
        ],
        credit_fee_handling='autem',
        due_date='nobis',
        integration=shared.ThreeBillionOneHundredAndNinetyMillionSixHundredAndEightyFiveThousandEightHundredAndThirtyTwoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461(
            quickbooks=shared.Sixad3f4f624fb518510130e879729b00ed8c237d1cebc5477abf34ac340a6424d(
                expense_account_id='nulla',
                item_id='voluptas',
            ),
        ),
        invoice_notes='libero',
        labels='tempora',
        late_fee_handling='explicabo',
        line_items=[
            shared.InvoiceLineItemsCreateRequest(
                cost_per_unit=553.74,
                description='molestiae',
                detail='magnam',
                discount='eius',
                integration='esse',
                labels={
                    "fuga": 'reprehenderit',
                },
                quantity=6956.26,
                reimbursable_expense=False,
                total_cost=2835.19,
                unit='eum',
            ),
        ],
        member='assumenda',
        member_client_id='eos',
        metadata=shared.InvoiceMetadata(
            purchase_order_number='quisquam',
        ),
        notification_preferences='ipsa',
        status=shared.StatusInvoiceUpdateRequest.PAYMENT_IN_TRANSIT,
    ),
    is_scheduling_only=False,
    labels='quo',
    payment_method_id='illum',
    schedule_dates=[
        shared.ScheduleDateUpdate(
            date_='fuga',
            invoice_template_id='eius',
            status=shared.StatusScheduleDateUpdate.PENDING,
        ),
    ],
    send_emails='ab',
    status=shared.StatusInvoiceTemplateUpdateRequest.EXPIRED,
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


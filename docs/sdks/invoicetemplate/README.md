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
    due_in_days=7301.22,
    frequency=[],
    invoice_data=shared.InvoiceDataCreateRequest(
        accepted_payment_methods=[
            shared.InvoiceDataCreateRequestAcceptedPaymentMethods.LESS_THAN_NIL_GREATER_THAN_,
        ],
        attachments=[],
        collaborators=[
            [],
        ],
        credit_fee_handling=[],
        currency=shared.CurrencyInvoiceDataCreateRequest.USD,
        due_date='quos',
        invoice_notes='aliquid',
        labels=[],
        late_fee_handling=[],
        line_items=[
            shared.InvoiceLineItemsCreateRequest(
                cost_per_unit=2123.9,
                description='dolorem',
                detail='dolor',
                discount=[],
                integration=[],
                labels=[],
                quantity=1861.93,
                reimbursable_expense=[],
                total_cost=2187.49,
                unit='hic',
            ),
        ],
        member_client_id='excepturi',
        notification_preferences=[],
        status=shared.StatusInvoiceDataCreateRequest.PAYMENT_IN_TRANSIT,
    ),
    is_scheduling_only=[],
    labels=[],
    schedule_dates=[
        [],
    ],
    send_emails=[],
    status=shared.StatusInvoiceTemplateCreateRequest.DRAFT,
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


res = s.invoice_template.delete(id='dignissimos')

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


res = s.invoice_template.get(id='reiciendis')

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


res = s.invoice_template.update(id='amet', invoice_template_update_request=shared.InvoiceTemplateUpdateRequest(
    account_id='dolorum',
    auto_payment_required=[],
    due_in_days=2543.56,
    frequency=[],
    invoice_data=[],
    is_scheduling_only=[],
    labels=[],
    payment_method_id='veritatis',
    schedule_dates=[
        [],
    ],
    send_emails=[],
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


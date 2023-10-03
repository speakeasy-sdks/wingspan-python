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
    due_in_days=4865.89,
    frequency=[],
    invoice_data=shared.InvoiceDataCreateRequest(
        accepted_payment_methods=[
            shared.InvoiceDataCreateRequestAcceptedPaymentMethods.ACH,
        ],
        attachments=[],
        collaborators=[
            [],
        ],
        credit_fee_handling=[],
        currency=shared.CurrencyInvoiceDataCreateRequest.CAD,
        due_date='Money blue shred',
        invoice_notes='technology East',
        labels=[],
        late_fee_handling=[],
        line_items=[
            shared.InvoiceLineItemsCreateRequest(
                cost_per_unit=1697.27,
                description='Front-line asynchronous paradigm',
                detail='SUV quantify Polestar',
                discount=[],
                integration=[],
                labels=[],
                quantity=4915.7,
                reimbursable_expense=[],
                total_cost=9574.09,
                unit='becquerel',
            ),
        ],
        member_client_id='Durham after',
        notification_preferences=[],
        status=shared.StatusInvoiceDataCreateRequest.PENDING,
    ),
    is_scheduling_only=[],
    labels=[],
    schedule_dates=[
        [],
    ],
    send_emails=[],
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


res = s.invoice_template.delete(id='program')

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


res = s.invoice_template.get(id='female')

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


res = s.invoice_template.update(id='Van', invoice_template_update_request=shared.InvoiceTemplateUpdateRequest(
    account_id='Reactive',
    auto_payment_required=[],
    due_in_days=9914.64,
    frequency=[],
    invoice_data=[],
    is_scheduling_only=[],
    labels=[],
    payment_method_id='Quality',
    schedule_dates=[
        [],
    ],
    send_emails=[],
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


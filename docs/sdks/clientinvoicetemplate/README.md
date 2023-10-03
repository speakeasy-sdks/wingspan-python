# ClientInvoiceTemplate
(*client_invoice_template*)

### Available Operations

* [create](#create) - Create client-invoice-template
* [get](#get) - Get client-invoice-template
* [update](#update) - Update client-invoice-template

## create

Create client-invoice-template

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()

req = shared.ClientInvoiceTemplateCreateRequest(
    account_id='bluetooth Extended',
    client_company='blue',
    client_email='grey technology East',
    client_email_cc=[
        'orange',
    ],
    client_first_name='male',
    client_last_name='Gasoline Screen mobile',
    due_in_days=6562.56,
    frequency=[],
    invoice_data=shared.ClientInvoiceDataCreateRequest(
        credit_fee_handling=[],
        currency=shared.CurrencyClientInvoiceDataCreateRequest.CAD,
        due_date='Fresh',
        line_items=[
            shared.InvoiceLineItemsCreateRequest(
                cost_per_unit=177.59,
                description='Open-architected contextually-based concept',
                detail='female',
                discount=[],
                integration=[],
                labels=[],
                quantity=8291.42,
                reimbursable_expense=[],
                total_cost=3229.97,
                unit='weber',
            ),
        ],
    ),
    member_id='Account',
    payment_method_id='Profound',
    schedule_dates=[
        [],
    ],
    status=shared.StatusClientInvoiceTemplateCreateRequest.ACTIVE,
)

res = s.client_invoice_template.create(req)

if res.client_invoice_template is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [shared.ClientInvoiceTemplateCreateRequest](../../models/shared/clientinvoicetemplatecreaterequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.CreateClientInvoiceTemplateResponse](../../models/operations/createclientinvoicetemplateresponse.md)**


## get

Get client-invoice-template

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.client_invoice_template.get(id='female')

if res.client_invoice_template is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.GetClientInvoiceTemplateResponse](../../models/operations/getclientinvoicetemplateresponse.md)**


## update

Update client-invoice-template

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()


res = s.client_invoice_template.update(id='Van', client_invoice_template_update_request=shared.ClientInvoiceTemplateUpdateRequest(
    account_id='Reactive',
    client_id='Metal cheater Islands',
    payment_method_id='withdrawal extend',
))

if res.client_invoice_template is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                             | *str*                                                                                                            | :heavy_check_mark:                                                                                               | Unique identifier                                                                                                |
| `client_invoice_template_update_request`                                                                         | [Optional[shared.ClientInvoiceTemplateUpdateRequest]](../../models/shared/clientinvoicetemplateupdaterequest.md) | :heavy_minus_sign:                                                                                               | N/A                                                                                                              |


### Response

**[operations.UpdateClientInvoiceTemplateResponse](../../models/operations/updateclientinvoicetemplateresponse.md)**


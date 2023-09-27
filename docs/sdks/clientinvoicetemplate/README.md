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
    account_id='id',
    client_company='labore',
    client_email='labore',
    client_email_cc=[
        'suscipit',
    ],
    client_first_name='natus',
    client_last_name='nobis',
    due_in_days=4287.69,
    frequency=[],
    invoice_data=shared.ClientInvoiceDataCreateRequest(
        credit_fee_handling=[],
        currency=shared.CurrencyClientInvoiceDataCreateRequest.LESS_THAN_NIL_GREATER_THAN_,
        due_date='aspernatur',
        line_items=[
            shared.InvoiceLineItemsCreateRequest(
                cost_per_unit=1028.63,
                description='magnam',
                detail='et',
                discount=[],
                integration=[],
                labels=[],
                quantity=5699.65,
                reimbursable_expense=[],
                total_cost=3540.47,
                unit='provident',
            ),
        ],
    ),
    member_id='quos',
    payment_method_id='sint',
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


res = s.client_invoice_template.get(id='mollitia')

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


res = s.client_invoice_template.update(id='reiciendis', client_invoice_template_update_request=shared.ClientInvoiceTemplateUpdateRequest(
    account_id='mollitia',
    client_id='ad',
    payment_method_id='eum',
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


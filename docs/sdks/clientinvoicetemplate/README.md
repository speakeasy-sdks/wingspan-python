# ClientInvoiceTemplate

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
    account_id='hic',
    client_company='recusandae',
    client_email='omnis',
    client_email_cc=[
        'facilis',
    ],
    client_first_name='perspiciatis',
    client_last_name='voluptatem',
    due_in_days=7836.45,
    frequency='blanditiis',
    invoice_data=shared.ClientInvoiceDataCreateRequest(
        credit_fee_handling=shared.FeeHandlingConfig(
            client_absolute_percentage=503.7,
            client_pays=5772.29,
            member_pays=6990.98,
        ),
        currency=shared.CurrencyClientInvoiceDataCreateRequest.USD,
        due_date='asperiores',
        line_items=[
            shared.InvoiceLineItemsCreateRequest(
                cost_per_unit=9342.14,
                description='modi',
                detail='iste',
                discount=shared.Facb8048736dba546c4c76242d9f8c7111011a7a7483528f37d80226698a1f2b(
                    amount=5356.33,
                    description='pariatur',
                    percentage=5899.1,
                ),
                integration=shared.ThreeBillionOneHundredAndNinetyMillionSixHundredAndEightyFiveThousandEightHundredAndThirtyTwoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461(
                    quickbooks=shared.Sixad3f4f624fb518510130e879729b00ed8c237d1cebc5477abf34ac340a6424d(
                        expense_account_id='delectus',
                        item_id='quaerat',
                    ),
                ),
                labels={
                    "aliquid": 'dolorem',
                },
                quantity=2098.43,
                reimbursable_expense='qui',
                total_cost=2187.49,
                unit='hic',
            ),
        ],
    ),
    member_id='excepturi',
    payment_method_id='cum',
    schedule_dates=[
        'dignissimos',
    ],
    status=shared.StatusClientInvoiceTemplateCreateRequest.CANCELLED,
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


res = s.client_invoice_template.get(id='amet')

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


res = s.client_invoice_template.update(id='dolorum', client_invoice_template_update_request=shared.ClientInvoiceTemplateUpdateRequest(
    account_id='numquam',
    client_id='veritatis',
    payment_method_id='ipsa',
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


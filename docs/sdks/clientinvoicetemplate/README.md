# client_invoice_template

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
    client_company='saepe',
    client_email='eius',
    client_email_cc=[
        'perferendis',
    ],
    client_first_name='amet',
    client_last_name='optio',
    due_in_days=8815.86,
    frequency='saepe',
    invoice_data=shared.ClientInvoiceDataCreateRequest(
        credit_fee_handling='deserunt',
        currency=shared.CurrencyClientInvoiceDataCreateRequest.CAD,
        due_date='minima',
        line_items=[
            shared.InvoiceLineItemsCreateRequest(
                cost_per_unit=5197.11,
                description='similique',
                detail='alias',
                discount=shared.Facb8048736dba546c4c76242d9f8c7111011a7a7483528f37d80226698a1f2b(
                    amount=3118.6,
                    description='tempora',
                    percentage=4254.51,
                ),
                integration=shared.ThreeBillionOneHundredAndNinetyMillionSixHundredAndEightyFiveThousandEightHundredAndThirtyTwoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461(
                    quickbooks=shared.Sixad3f4f624fb518510130e879729b00ed8c237d1cebc5477abf34ac340a6424d(
                        expense_account_id='qui',
                        item_id='dolorum',
                    ),
                ),
                labels={
                    "harum": 'iusto',
                    "ipsum": 'quisquam',
                },
                quantity=9473.71,
                reimbursable_expense='tempore',
                total_cost=8802.98,
                unit='numquam',
            ),
            shared.InvoiceLineItemsCreateRequest(
                cost_per_unit=3136.92,
                description='dolorem',
                detail='sapiente',
                discount=shared.Facb8048736dba546c4c76242d9f8c7111011a7a7483528f37d80226698a1f2b(
                    amount=4717.52,
                    description='sit',
                    percentage=7115.84,
                ),
                integration='sed',
                labels='libero',
                quantity=3741.7,
                reimbursable_expense=False,
                total_cost=4635.75,
                unit='ipsum',
            ),
            shared.InvoiceLineItemsCreateRequest(
                cost_per_unit=2776.28,
                description='qui',
                detail='cupiditate',
                discount=shared.Facb8048736dba546c4c76242d9f8c7111011a7a7483528f37d80226698a1f2b(
                    amount=8638.56,
                    description='soluta',
                    percentage=1175.31,
                ),
                integration=shared.ThreeBillionOneHundredAndNinetyMillionSixHundredAndEightyFiveThousandEightHundredAndThirtyTwoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461(
                    quickbooks=shared.Sixad3f4f624fb518510130e879729b00ed8c237d1cebc5477abf34ac340a6424d(
                        expense_account_id='incidunt',
                        item_id='aspernatur',
                    ),
                ),
                labels='distinctio',
                quantity=7044.74,
                reimbursable_expense='quam',
                total_cost=5654.21,
                unit='temporibus',
            ),
            shared.InvoiceLineItemsCreateRequest(
                cost_per_unit=1832.8,
                description='neque',
                detail='fugit',
                discount='odio',
                integration='ullam',
                labels={
                    "voluptatem": 'cumque',
                    "soluta": 'nobis',
                    "et": 'saepe',
                    "ipsum": 'veritatis',
                },
                quantity=7492.55,
                reimbursable_expense=False,
                total_cost=7316.94,
                unit='cupiditate',
            ),
        ],
    ),
    member_id='aperiam',
    payment_method_id='delectus',
    schedule_dates=[
        'labore',
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


res = s.client_invoice_template.get(id='dolorum')

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


res = s.client_invoice_template.update(id='architecto', client_invoice_template_update_request=shared.ClientInvoiceTemplateUpdateRequest(
    account_id='quae',
    client_id='aut',
    payment_method_id='quas',
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


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
    account_id='consequuntur',
    client_company='blanditiis',
    client_email='error',
    client_email_cc=[
        'eaque',
    ],
    client_first_name='occaecati',
    client_last_name='rerum',
    due_in_days=2378.93,
    frequency=shared.Frequency(
        daily=False,
        day_in_interval=2672.62,
        end_date='iste',
        every=6790.91,
        interval=shared.IntervalFrequency.MONTH,
        start_date='pariatur',
        twice_per_month=False,
    ),
    invoice_data=shared.ClientInvoiceDataCreateRequest(
        credit_fee_handling=shared.FeeHandlingConfig(
            client_absolute_percentage=7301.22,
            client_pays=9644.9,
            member_pays=3119.45,
        ),
        currency=shared.CurrencyClientInvoiceDataCreateRequest.CAD,
        due_date='aliquid',
        line_items=[
            shared.InvoiceLineItemsCreateRequest(
                cost_per_unit=2123.9,
                description='dolorem',
                detail='dolor',
                discount='ipsum',
                integration=shared.ThreeBillionOneHundredAndNinetyMillionSixHundredAndEightyFiveThousandEightHundredAndThirtyTwoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461(
                    quickbooks=shared.Sixad3f4f624fb518510130e879729b00ed8c237d1cebc5477abf34ac340a6424d(
                        expense_account_id='cum',
                        item_id='voluptate',
                    ),
                ),
                labels='reiciendis',
                quantity=2274.14,
                reimbursable_expense=False,
                total_cost=2543.56,
                unit='veritatis',
            ),
        ],
    ),
    member_id='ipsa',
    payment_method_id='ipsa',
    schedule_dates=[
        'odio',
    ],
    status=shared.StatusClientInvoiceTemplateCreateRequest.DRAFT,
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


res = s.client_invoice_template.get(id='accusamus')

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


res = s.client_invoice_template.update(id='quidem', client_invoice_template_update_request=shared.ClientInvoiceTemplateUpdateRequest(
    account_id='voluptatibus',
    client_id='voluptas',
    payment_method_id='natus',
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


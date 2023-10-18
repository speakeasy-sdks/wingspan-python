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
    client_email='online',
    client_email_cc=[
        'Configuration',
    ],
    frequency=shared.Frequency(
        start_date='Money',
    ),
    invoice_data=shared.ClientInvoiceDataCreateRequest(
        credit_fee_handling=shared.FeeHandlingConfig(),
        line_items=[
            shared.InvoiceLineItemsCreateRequest(
                discount=shared.Facb8048736dba546c4c76242d9f8c7111011a7a7483528f37d80226698a1f2b(),
                integration=shared.ThreeBillionOneHundredAndNinetyMillionSixHundredAndEightyFiveThousandEightHundredAndThirtyTwoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461(
                    quickbooks=shared.Sixad3f4f624fb518510130e879729b00ed8c237d1cebc5477abf34ac340a6424d(),
                ),
                labels={
                    "blue": 'shred',
                },
            ),
        ],
    ),
    member_id='abnormally',
    schedule_dates=[
        shared.ScheduleDate(
            date_='deposit',
            status=shared.StatusScheduleDate.COMPLETED,
        ),
    ],
    status=shared.StatusClientInvoiceTemplateCreateRequest.ACTIVE,
)

res = s.client_invoice_template.create(req)

if res.client_invoice_template is not None:
    # handle response
    pass
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
    pass
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
    client_id='East',
))

if res.client_invoice_template is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                             | *str*                                                                                                            | :heavy_check_mark:                                                                                               | Unique identifier                                                                                                |
| `client_invoice_template_update_request`                                                                         | [Optional[shared.ClientInvoiceTemplateUpdateRequest]](../../models/shared/clientinvoicetemplateupdaterequest.md) | :heavy_minus_sign:                                                                                               | N/A                                                                                                              |


### Response

**[operations.UpdateClientInvoiceTemplateResponse](../../models/operations/updateclientinvoicetemplateresponse.md)**


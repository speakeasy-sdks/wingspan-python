# InvoiceAsClient

### Available Operations

* [create](#create) - Create invoice as client

## create

Create invoice as client

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()

req = shared.ClientInvoiceCreateRequest(
    client_company='et',
    client_email='saepe',
    client_email_cc=[
        'ipsum',
    ],
    client_first_name='veritatis',
    client_last_name='nobis',
    credit_fee_handling=shared.FeeHandlingConfig(
        client_absolute_percentage=7316.94,
        client_pays=5844.76,
        member_pays=456.14,
    ),
    currency=shared.CurrencyClientInvoiceCreateRequest.LESS_THAN_NIL_GREATER_THAN_,
    due_date='dolorem',
    line_items=[
        shared.InvoiceLineItemsCreateRequest(
            cost_per_unit=2921.47,
            description='labore',
            detail='adipisci',
            discount=shared.Facb8048736dba546c4c76242d9f8c7111011a7a7483528f37d80226698a1f2b(
                amount=1002.94,
                description='quae',
                percentage=164.29,
            ),
            integration=shared.ThreeBillionOneHundredAndNinetyMillionSixHundredAndEightyFiveThousandEightHundredAndThirtyTwoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461(
                quickbooks=shared.Sixad3f4f624fb518510130e879729b00ed8c237d1cebc5477abf34ac340a6424d(
                    expense_account_id='consequatur',
                    item_id='est',
                ),
            ),
            labels={
                "porro": 'doloribus',
            },
            quantity=2817.3,
            reimbursable_expense=False,
            total_cost=5864.1,
            unit='qui',
        ),
    ],
    member_id='quae',
)

res = s.invoice_as_client.create(req)

if res.client_invoice is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [shared.ClientInvoiceCreateRequest](../../models/shared/clientinvoicecreaterequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.CreateInvoiceAsClientResponse](../../models/operations/createinvoiceasclientresponse.md)**


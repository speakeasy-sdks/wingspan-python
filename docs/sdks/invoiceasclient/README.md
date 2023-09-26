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
    client_company='voluptatibus',
    client_email='quisquam',
    client_email_cc=[
        'vero',
    ],
    client_first_name='omnis',
    client_last_name='quis',
    credit_fee_handling='delectus',
    currency=shared.CurrencyClientInvoiceCreateRequest.CAD,
    due_date='consectetur',
    line_items=[
        shared.InvoiceLineItemsCreateRequest(
            cost_per_unit=8788.7,
            description='tenetur',
            detail='dignissimos',
            discount=shared.Facb8048736dba546c4c76242d9f8c7111011a7a7483528f37d80226698a1f2b(
                amount=7155.61,
                description='quod',
                percentage=4861.6,
            ),
            integration=shared.ThreeBillionOneHundredAndNinetyMillionSixHundredAndEightyFiveThousandEightHundredAndThirtyTwoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461(
                quickbooks=shared.Sixad3f4f624fb518510130e879729b00ed8c237d1cebc5477abf34ac340a6424d(
                    expense_account_id='vero',
                    item_id='ducimus',
                ),
            ),
            labels='quibusdam',
            quantity=8489.44,
            reimbursable_expense='natus',
            total_cost=7733.26,
            unit='aut',
        ),
    ],
    member_id='voluptatibus',
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


# InvoiceAsClient
(*invoice_as_client*)

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
    client_email='string',
    client_email_cc=[
        'string',
    ],
    credit_fee_handling=shared.FeeHandlingConfig(),
    due_date='string',
    line_items=[
        shared.InvoiceLineItemsCreateRequest(
            discount=shared.Facb8048736dba546c4c76242d9f8c7111011a7a7483528f37d80226698a1f2b(),
            integration=shared.ThreeBillionOneHundredAndNinetyMillionSixHundredAndEightyFiveThousandEightHundredAndThirtyTwoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461(
                quickbooks=shared.Sixad3f4f624fb518510130e879729b00ed8c237d1cebc5477abf34ac340a6424d(),
            ),
            labels={
                "key": 'string',
            },
        ),
    ],
    member_id='string',
)

res = s.invoice_as_client.create(req)

if res.client_invoice is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [shared.ClientInvoiceCreateRequest](../../models/shared/clientinvoicecreaterequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.CreateInvoiceAsClientResponse](../../models/operations/createinvoiceasclientresponse.md)**


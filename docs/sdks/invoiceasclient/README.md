# invoice_as_client

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
    client_company='ipsam',
    client_email='aspernatur',
    client_email_cc=[
        'quo',
    ],
    client_first_name='esse',
    client_last_name='recusandae',
    credit_fee_handling='distinctio',
    currency=shared.CurrencyClientInvoiceCreateRequest.LESS_THAN_NIL_GREATER_THAN_,
    due_date='dignissimos',
    line_items=[
        shared.InvoiceLineItemsCreateRequest(
            cost_per_unit=4694.98,
            description='totam',
            detail='accusamus',
            discount='odio',
            integration=shared.ThreeBillionOneHundredAndNinetyMillionSixHundredAndEightyFiveThousandEightHundredAndThirtyTwoa4970525ea5b0803efff0b36a0202062e1fd8a0bc187acbe156461(
                quickbooks='sapiente',
            ),
            labels='deserunt',
            quantity=4752.89,
            reimbursable_expense='porro',
            total_cost=4304.02,
            unit='quas',
        ),
    ],
    member_id='praesentium',
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


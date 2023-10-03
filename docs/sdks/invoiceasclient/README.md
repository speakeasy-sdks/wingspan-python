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
    client_company='bluetooth Extended',
    client_email='blue',
    client_email_cc=[
        'shred',
    ],
    client_first_name='technology East',
    client_last_name='evolve',
    credit_fee_handling=[],
    currency=shared.CurrencyClientInvoiceCreateRequest.LESS_THAN_NIL_GREATER_THAN_,
    due_date='SUV quantify Polestar',
    line_items=[
        shared.InvoiceLineItemsCreateRequest(
            cost_per_unit=4915.7,
            description='User-friendly multi-state frame',
            detail='Fresh',
            discount=[],
            integration=[],
            labels=[],
            quantity=177.59,
            reimbursable_expense=[],
            total_cost=5190.28,
            unit='kilogram',
        ),
    ],
    member_id='Fish',
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


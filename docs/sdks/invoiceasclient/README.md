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
    client_company='blanditiis',
    client_email='error',
    client_email_cc=[
        'eaque',
    ],
    client_first_name='occaecati',
    client_last_name='rerum',
    credit_fee_handling=[],
    currency=shared.CurrencyClientInvoiceCreateRequest.USD,
    due_date='asperiores',
    line_items=[
        shared.InvoiceLineItemsCreateRequest(
            cost_per_unit=9342.14,
            description='modi',
            detail='iste',
            discount=[],
            integration=[],
            labels=[],
            quantity=6790.91,
            reimbursable_expense=[],
            total_cost=5356.33,
            unit='pariatur',
        ),
    ],
    member_id='provident',
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


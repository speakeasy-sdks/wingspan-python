# PayableOnClient
(*payable_on_client*)

### Available Operations

* [create](#create) - Create payable on client for member
* [update](#update) - Update payable on client by payableId

## create

Create payable on client for member

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()

req = shared.PayableCreateRequest(
    accepted_payment_methods=[
        shared.PayableCreateRequestAcceptedPaymentMethods.ACH,
    ],
    attachments=[],
    client=[],
    collaborator_id='Configuration Money',
    credit_fee_handling=shared.FeeHandlingConfig(
        client_absolute_percentage=7865.46,
        client_pays=690.25,
        member_pays=9967.06,
    ),
    currency=shared.CurrencyPayableCreateRequest.LESS_THAN_NIL_GREATER_THAN_,
    due_date='technology East',
    integration=[],
    invoice_notes='evolve',
    labels=[],
    late_fee_handling=[],
    line_items=[
        shared.InvoiceLineItemsCreateRequest(
            cost_per_unit=7150.4,
            description='Secured systematic protocol',
            detail='Screen mobile',
            discount=[],
            integration=[],
            labels=[],
            quantity=6562.56,
            reimbursable_expense=[],
            total_cost=3570.21,
            unit='meter',
        ),
    ],
    member=[],
    member_client_id='after',
    metadata=[],
    notification_preferences=[],
    status=shared.StatusPayableCreateRequest.PENDING,
)

res = s.payable_on_client.create(req)

if res.payable_schema is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [shared.PayableCreateRequest](../../models/shared/payablecreaterequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.CreatePayableOnClientResponse](../../models/operations/createpayableonclientresponse.md)**


## update

Update payable on client by payableId

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()


res = s.payable_on_client.update(id='Van', payable_update_request=shared.PayableUpdateRequest(
    accepted_payment_methods=[
        shared.PayableUpdateRequestAcceptedPaymentMethods.CREDIT,
    ],
    attachments=[],
    charged_fees=[],
    client=[],
    collaborators=[
        [],
    ],
    credit_fee_handling=[],
    due_date='male Metal',
    integration=[],
    invoice_notes='Arizona Cotton extend',
    labels=[],
    late_fee_handling=[],
    line_items=[
        [],
    ],
    member=[],
    member_client_id='bifurcated',
    metadata=[],
    notification_preferences=[],
    payment_methods=[
        shared.PayableUpdateRequestPaymentMethods.MANUAL,
    ],
    status=shared.StatusPayableUpdateRequest.PAID,
))

if res.payable_schema is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `id`                                                                                 | *str*                                                                                | :heavy_check_mark:                                                                   | Unique identifier                                                                    |
| `payable_update_request`                                                             | [Optional[shared.PayableUpdateRequest]](../../models/shared/payableupdaterequest.md) | :heavy_minus_sign:                                                                   | N/A                                                                                  |


### Response

**[operations.UpdatePayableOnClientResponse](../../models/operations/updatepayableonclientresponse.md)**


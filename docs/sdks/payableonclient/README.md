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
        shared.PayableCreateRequestAcceptedPaymentMethods.LESS_THAN_NIL_GREATER_THAN_,
    ],
    attachments=[],
    client=[],
    collaborator_id='tenetur',
    credit_fee_handling=shared.FeeHandlingConfig(
        client_absolute_percentage=2294.42,
        client_pays=7308.56,
        member_pays=8802.98,
    ),
    currency=shared.CurrencyPayableCreateRequest.USD,
    due_date='enim',
    integration=[],
    invoice_notes='dolorem',
    labels=[],
    late_fee_handling=[],
    line_items=[
        shared.InvoiceLineItemsCreateRequest(
            cost_per_unit=9574.51,
            description='totam',
            detail='nihil',
            discount=[],
            integration=[],
            labels=[],
            quantity=256.62,
            reimbursable_expense=[],
            total_cost=7115.84,
            unit='neque',
        ),
    ],
    member=[],
    member_client_id='sed',
    metadata=[],
    notification_preferences=[],
    status=shared.StatusPayableCreateRequest.CANCELLED,
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


res = s.payable_on_client.update(id='libero', payable_update_request=shared.PayableUpdateRequest(
    accepted_payment_methods=[
        shared.PayableUpdateRequestAcceptedPaymentMethods.ACH,
    ],
    attachments=[],
    charged_fees=[],
    client=[],
    collaborators=[
        [],
    ],
    credit_fee_handling=[],
    due_date='deserunt',
    integration=[],
    invoice_notes='quam',
    labels=[],
    late_fee_handling=[],
    line_items=[
        [],
    ],
    member=[],
    member_client_id='ipsum',
    metadata=[],
    notification_preferences=[],
    payment_methods=[
        shared.PayableUpdateRequestPaymentMethods.ACH,
    ],
    status=shared.StatusPayableUpdateRequest.OPEN,
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


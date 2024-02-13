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
    collaborator_id='string',
    credit_fee_handling=shared.FeeHandlingConfig(),
    due_date='string',
    line_items=[
        shared.InvoiceLineItemsCreateRequest(),
    ],
)

res = s.payable_on_client.create(req)

if res.payable_schema is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [shared.PayableCreateRequest](../../models/shared/payablecreaterequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.CreatePayableOnClientResponse](../../models/operations/createpayableonclientresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update

Update payable on client by payableId

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()


res = s.payable_on_client.update(id='string', payable_update_request=shared.PayableUpdateRequest())

if res.payable_schema is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `id`                                                                                 | *str*                                                                                | :heavy_check_mark:                                                                   | Unique identifier                                                                    |
| `payable_update_request`                                                             | [Optional[shared.PayableUpdateRequest]](../../models/shared/payableupdaterequest.md) | :heavy_minus_sign:                                                                   | N/A                                                                                  |


### Response

**[operations.UpdatePayableOnClientResponse](../../models/operations/updatepayableonclientresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

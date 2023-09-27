# CollaboratorDeduction
(*collaborator_deduction*)

### Available Operations

* [create](#create) - Create deduction
* [delete](#delete) - Delete deduction
* [get](#get) - Get deduction
* [update](#update) - Update deduction

## create

Create deduction

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()

req = shared.DeductionCreateRequest(
    amount=995.69,
    client_id='repudiandae',
    currency=shared.DeductionCreateRequestCurrency.USD,
    member_id='expedita',
    name='Kristie Spencer',
    priority=8681.26,
    source_invoice_id='accusantium',
    start_date='consequuntur',
    type=shared.TypeDeductionCreateRequest.POST_PAYMENT,
)

res = s.collaborator_deduction.create(req)

if res.deduction_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.DeductionCreateRequest](../../models/shared/deductioncreaterequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.CreateCollaboratorDeductionResponse](../../models/operations/createcollaboratordeductionresponse.md)**


## delete

Delete deduction

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.collaborator_deduction.delete(id='natus')

if res.deduction_response is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.DeleteCollaboratorDeductionResponse](../../models/operations/deletecollaboratordeductionresponse.md)**


## get

Get deduction

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.collaborator_deduction.get(id='magni')

if res.deduction_response is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.GetCollaboratorDeductionResponse](../../models/operations/getcollaboratordeductionresponse.md)**


## update

Update deduction

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()


res = s.collaborator_deduction.update(id='sunt', deduction_update_request=shared.DeductionUpdateRequest(
    amount=7790.51,
    currency=shared.CurrencyDeductionUpdateRequest.LESS_THAN_NIL_GREATER_THAN_,
    name='Simon Jenkins',
    priority=4071.83,
    source_invoice_id='accusantium',
    start_date='ab',
    type=shared.TypeDeductionUpdateRequest.LESS_THAN_NIL_GREATER_THAN_,
))

if res.deduction_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `id`                                                                                     | *str*                                                                                    | :heavy_check_mark:                                                                       | Unique identifier                                                                        |
| `deduction_update_request`                                                               | [Optional[shared.DeductionUpdateRequest]](../../models/shared/deductionupdaterequest.md) | :heavy_minus_sign:                                                                       | N/A                                                                                      |


### Response

**[operations.UpdateCollaboratorDeductionResponse](../../models/operations/updatecollaboratordeductionresponse.md)**


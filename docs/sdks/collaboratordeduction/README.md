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
    amount=4865.89,
    client_id='string',
    currency=shared.DeductionCreateRequestCurrency.USD,
    member_id='string',
    name='string',
    type=shared.TypeDeductionCreateRequest.POST_PAYMENT,
)

res = s.collaborator_deduction.create(req)

if res.deduction_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.DeductionCreateRequest](../../models/shared/deductioncreaterequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.CreateCollaboratorDeductionResponse](../../models/operations/createcollaboratordeductionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete

Delete deduction

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.collaborator_deduction.delete(id='string')

if res.deduction_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.DeleteCollaboratorDeductionResponse](../../models/operations/deletecollaboratordeductionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get

Get deduction

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.collaborator_deduction.get(id='string')

if res.deduction_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.GetCollaboratorDeductionResponse](../../models/operations/getcollaboratordeductionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update

Update deduction

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()


res = s.collaborator_deduction.update(id='string', deduction_update_request=shared.DeductionUpdateRequest())

if res.deduction_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `id`                                                                                     | *str*                                                                                    | :heavy_check_mark:                                                                       | Unique identifier                                                                        |
| `deduction_update_request`                                                               | [Optional[shared.DeductionUpdateRequest]](../../models/shared/deductionupdaterequest.md) | :heavy_minus_sign:                                                                       | N/A                                                                                      |


### Response

**[operations.UpdateCollaboratorDeductionResponse](../../models/operations/updatecollaboratordeductionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

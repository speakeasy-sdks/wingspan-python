# ClientDeductionID
(*client_deduction_id*)

### Available Operations

* [delete](#delete) - Delete deduction
* [get](#get) - Get deduction
* [update](#update) - Update deduction

## delete

Delete deduction

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.client_deduction_id.delete(id='string')

if res.deduction_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.DeleteClientDeductionIDResponse](../../models/operations/deleteclientdeductionidresponse.md)**
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


res = s.client_deduction_id.get(id='string')

if res.deduction_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.GetClientDeductionIDResponse](../../models/operations/getclientdeductionidresponse.md)**
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


res = s.client_deduction_id.update(id='string', deduction_update_request=shared.DeductionUpdateRequest())

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

**[operations.UpdateClientDeductionIDResponse](../../models/operations/updateclientdeductionidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

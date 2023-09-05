# client_deduction_id

### Available Operations

* [delete](#delete) - Delete deduction
* [get](#get) - Get deduction
* [update](#update) - Update deduction

## delete

Delete deduction

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.client_deduction_id.delete(id='iure')

if res.deduction_response is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.DeleteClientDeductionIDResponse](../../models/operations/deleteclientdeductionidresponse.md)**


## get

Get deduction

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.client_deduction_id.get(id='odio')

if res.deduction_response is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.GetClientDeductionIDResponse](../../models/operations/getclientdeductionidresponse.md)**


## update

Update deduction

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()


res = s.client_deduction_id.update(id='quaerat', deduction_update_request=shared.DeductionUpdateRequest(
    amount=8810.05,
    currency=shared.CurrencyDeductionUpdateRequest.LESS_THAN_NIL_GREATER_THAN_,
    name='Hector Mosciski',
    priority=246.78,
    source_invoice_id='fugiat',
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

**[operations.UpdateClientDeductionIDResponse](../../models/operations/updateclientdeductionidresponse.md)**


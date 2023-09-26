# ClientDeductionID

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


res = s.client_deduction_id.delete(id='cumque')

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


res = s.client_deduction_id.get(id='corporis')

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


res = s.client_deduction_id.update(id='hic', deduction_update_request=shared.DeductionUpdateRequest(
    amount=7299.91,
    currency=shared.CurrencyDeductionUpdateRequest.LESS_THAN_NIL_GREATER_THAN_,
    name='Beatrice Lebsack II',
    priority=1999.96,
    source_invoice_id='eos',
    start_date='perferendis',
    type=shared.TypeDeductionUpdateRequest.PRE_PAYMENT,
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


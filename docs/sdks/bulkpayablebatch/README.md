# bulk_payable_batch

### Available Operations

* [create](#create) - Create a bulk payable batch
* [delete](#delete) - Delete a bulk payable batch
* [get](#get) - Get a bulk payable batch
* [update](#update) - Update a bulk payable batch

## create

Create a bulk payable batch

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()

req = shared.BulkPayableBatchCreate(
    labels='autem',
    processing_strategy=shared.BulkPayableBatchCreateProcessingStrategy.SINGLE,
)

res = s.bulk_payable_batch.create(req)

if res.bulk_payable_batch is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.BulkPayableBatchCreate](../../models/shared/bulkpayablebatchcreate.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.CreateBulkPayableBatchResponse](../../models/operations/createbulkpayablebatchresponse.md)**


## delete

Delete a bulk payable batch

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.bulk_payable_batch.delete(batch_id='eaque')

if res.bulk_payable_batch is not None:
    # handle response
```

### Parameters

| Parameter                     | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `batch_id`                    | *str*                         | :heavy_check_mark:            | Unique identifier for a batch |


### Response

**[operations.DeleteBulkPayableBatchResponse](../../models/operations/deletebulkpayablebatchresponse.md)**


## get

Get a bulk payable batch

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.bulk_payable_batch.get(batch_id='pariatur')

if res.bulk_payable_batch is not None:
    # handle response
```

### Parameters

| Parameter                     | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `batch_id`                    | *str*                         | :heavy_check_mark:            | Unique identifier for a batch |


### Response

**[operations.GetBulkPayableBatchResponse](../../models/operations/getbulkpayablebatchresponse.md)**


## update

Update a bulk payable batch

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()


res = s.bulk_payable_batch.update(batch_id='nemo', bulk_payable_batch_update=shared.BulkPayableBatchUpdate(
    labels={
        "fugiat": 'amet',
    },
    status=shared.StatusBulkPayableBatchUpdate.OPEN,
))

if res.bulk_payable_batch is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `batch_id`                                                                               | *str*                                                                                    | :heavy_check_mark:                                                                       | Unique identifier for a batch                                                            |
| `bulk_payable_batch_update`                                                              | [Optional[shared.BulkPayableBatchUpdate]](../../models/shared/bulkpayablebatchupdate.md) | :heavy_minus_sign:                                                                       | N/A                                                                                      |


### Response

**[operations.UpdateBulkPayableBatchResponse](../../models/operations/updatebulkpayablebatchresponse.md)**


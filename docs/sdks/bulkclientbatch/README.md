# BulkClientBatch

### Available Operations

* [create](#create) - Create a bulk client batch
* [get](#get) - Get a bulk client batch
* [update](#update) - Update a bulk client batch

## create

Create a bulk client batch

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()

req = shared.BulkBatchCreate(
    labels='iste',
)

res = s.bulk_client_batch.create(req)

if res.bulk_client_batch is not None:
    # handle response
```

### Parameters

| Parameter                                                        | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `request`                                                        | [shared.BulkBatchCreate](../../models/shared/bulkbatchcreate.md) | :heavy_check_mark:                                               | The request object to use for the request.                       |


### Response

**[operations.CreateBulkClientBatchResponse](../../models/operations/createbulkclientbatchresponse.md)**


## get

Get a bulk client batch

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.bulk_client_batch.get(batch_id='dolor')

if res.bulk_client_batch is not None:
    # handle response
```

### Parameters

| Parameter                     | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `batch_id`                    | *str*                         | :heavy_check_mark:            | Unique identifier for a batch |


### Response

**[operations.GetBulkClientBatchResponse](../../models/operations/getbulkclientbatchresponse.md)**


## update

Update a bulk client batch

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()


res = s.bulk_client_batch.update(batch_id='natus', bulk_batch_update=shared.BulkBatchUpdate(
    labels='hic',
    status=shared.StatusBulkBatchUpdate.LESS_THAN_NIL_GREATER_THAN_,
))

if res.bulk_client_batch is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `batch_id`                                                                 | *str*                                                                      | :heavy_check_mark:                                                         | Unique identifier for a batch                                              |
| `bulk_batch_update`                                                        | [Optional[shared.BulkBatchUpdate]](../../models/shared/bulkbatchupdate.md) | :heavy_minus_sign:                                                         | N/A                                                                        |


### Response

**[operations.UpdateBulkClientBatchResponse](../../models/operations/updatebulkclientbatchresponse.md)**


# BulkClientBatch
(*bulk_client_batch*)

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

req = shared.BulkBatchCreate()

res = s.bulk_client_batch.create(req)

if res.bulk_client_batch is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                        | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `request`                                                        | [shared.BulkBatchCreate](../../models/shared/bulkbatchcreate.md) | :heavy_check_mark:                                               | The request object to use for the request.                       |


### Response

**[operations.CreateBulkClientBatchResponse](../../models/operations/createbulkclientbatchresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get

Get a bulk client batch

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.bulk_client_batch.get(batch_id='<value>')

if res.bulk_client_batch is not None:
    # handle response
    pass

```

### Parameters

| Parameter                     | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `batch_id`                    | *str*                         | :heavy_check_mark:            | Unique identifier for a batch |


### Response

**[operations.GetBulkClientBatchResponse](../../models/operations/getbulkclientbatchresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update

Update a bulk client batch

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()


res = s.bulk_client_batch.update(batch_id='<value>', bulk_batch_update=shared.BulkBatchUpdate())

if res.bulk_client_batch is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `batch_id`                                                                 | *str*                                                                      | :heavy_check_mark:                                                         | Unique identifier for a batch                                              |
| `bulk_batch_update`                                                        | [Optional[shared.BulkBatchUpdate]](../../models/shared/bulkbatchupdate.md) | :heavy_minus_sign:                                                         | N/A                                                                        |


### Response

**[operations.UpdateBulkClientBatchResponse](../../models/operations/updatebulkclientbatchresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

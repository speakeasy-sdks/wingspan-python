# BulkCollaboratorBatch
(*bulk_collaborator_batch*)

### Available Operations

* [create](#create) - Create a bulk collaborator batch
* [get](#get) - Get a bulk collaborator batch
* [update](#update) - Update a bulk collaborator batch

## create

Create a bulk collaborator batch

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()

req = shared.BulkBatchCreate()

res = s.bulk_collaborator_batch.create(req)

if res.bulk_collaborator_batch is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                        | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `request`                                                        | [shared.BulkBatchCreate](../../models/shared/bulkbatchcreate.md) | :heavy_check_mark:                                               | The request object to use for the request.                       |


### Response

**[operations.CreateBulkCollaboratorBatchResponse](../../models/operations/createbulkcollaboratorbatchresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get

Get a bulk collaborator batch

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.bulk_collaborator_batch.get(batch_id='<value>')

if res.bulk_collaborator_batch is not None:
    # handle response
    pass

```

### Parameters

| Parameter                     | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `batch_id`                    | *str*                         | :heavy_check_mark:            | Unique identifier for a batch |


### Response

**[operations.GetBulkCollaboratorBatchResponse](../../models/operations/getbulkcollaboratorbatchresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update

Update a bulk collaborator batch

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()


res = s.bulk_collaborator_batch.update(batch_id='<value>', bulk_batch_update=shared.BulkBatchUpdate())

if res.bulk_collaborator_batch is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `batch_id`                                                                 | *str*                                                                      | :heavy_check_mark:                                                         | Unique identifier for a batch                                              |
| `bulk_batch_update`                                                        | [Optional[shared.BulkBatchUpdate]](../../models/shared/bulkbatchupdate.md) | :heavy_minus_sign:                                                         | N/A                                                                        |


### Response

**[operations.UpdateBulkCollaboratorBatchResponse](../../models/operations/updatebulkcollaboratorbatchresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

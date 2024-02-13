# BulkCollaboratorBatchItem
(*bulk_collaborator_batch_item*)

### Available Operations

* [create](#create) - Create a bulk collaborator batch item
* [get](#get) - Get a bulk collaborator batch item
* [update](#update) - Update a bulk collaborator batch item

## create

Create a bulk collaborator batch item

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()


res = s.bulk_collaborator_batch_item.create(batch_id='string', bulk_collaborator_item_create=shared.BulkCollaboratorItemCreate())

if res.bulk_collaborator_item is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `batch_id`                                                                                       | *str*                                                                                            | :heavy_check_mark:                                                                               | Unique identifier for a batch                                                                    |
| `bulk_collaborator_item_create`                                                                  | [Optional[shared.BulkCollaboratorItemCreate]](../../models/shared/bulkcollaboratoritemcreate.md) | :heavy_minus_sign:                                                                               | N/A                                                                                              |


### Response

**[operations.CreateBulkCollaboratorBatchItemResponse](../../models/operations/createbulkcollaboratorbatchitemresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get

Get a bulk collaborator batch item

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.bulk_collaborator_batch_item.get(batch_id='string', batch_item_id='string')

if res.bulk_collaborator_item is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                | Type                                     | Required                                 | Description                              |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `batch_id`                               | *str*                                    | :heavy_check_mark:                       | Unique identifier for a batch            |
| `batch_item_id`                          | *str*                                    | :heavy_check_mark:                       | Unique identifier for an item in a batch |


### Response

**[operations.GetBulkCollaboratorBatchItemResponse](../../models/operations/getbulkcollaboratorbatchitemresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update

Update a bulk collaborator batch item

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()


res = s.bulk_collaborator_batch_item.update(batch_id='string', batch_item_id='string', bulk_collaborator_item_update=shared.BulkCollaboratorItemUpdate())

if res.bulk_collaborator_item is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `batch_id`                                                                                       | *str*                                                                                            | :heavy_check_mark:                                                                               | Unique identifier for a batch                                                                    |
| `batch_item_id`                                                                                  | *str*                                                                                            | :heavy_check_mark:                                                                               | Unique identifier for an item in a batch                                                         |
| `bulk_collaborator_item_update`                                                                  | [Optional[shared.BulkCollaboratorItemUpdate]](../../models/shared/bulkcollaboratoritemupdate.md) | :heavy_minus_sign:                                                                               | N/A                                                                                              |


### Response

**[operations.UpdateBulkCollaboratorBatchItemResponse](../../models/operations/updatebulkcollaboratorbatchitemresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

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
from wingspan.models import operations, shared

s = wingspan.Wingspan()


res = s.bulk_collaborator_batch_item.create(batch_id='omnis', bulk_collaborator_item_create=shared.BulkCollaboratorItemCreate(
    collaborator_group_id='nemo',
    collaborator_id='minima',
    collaborator_status=shared.CollaboratorStatusBulkCollaboratorItemCreate.PENDING,
    company='Kessler LLC',
    email='Veronica.Brakus@hotmail.com',
    external_id='culpa',
    first_last_name='consequuntur',
    form_w9_data=[],
    labels=[],
))

if res.bulk_collaborator_item is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `batch_id`                                                                                       | *str*                                                                                            | :heavy_check_mark:                                                                               | Unique identifier for a batch                                                                    |
| `bulk_collaborator_item_create`                                                                  | [Optional[shared.BulkCollaboratorItemCreate]](../../models/shared/bulkcollaboratoritemcreate.md) | :heavy_minus_sign:                                                                               | N/A                                                                                              |


### Response

**[operations.CreateBulkCollaboratorBatchItemResponse](../../models/operations/createbulkcollaboratorbatchitemresponse.md)**


## get

Get a bulk collaborator batch item

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.bulk_collaborator_batch_item.get(batch_id='repellat', batch_item_id='mollitia')

if res.bulk_collaborator_item is not None:
    # handle response
```

### Parameters

| Parameter                                | Type                                     | Required                                 | Description                              |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `batch_id`                               | *str*                                    | :heavy_check_mark:                       | Unique identifier for a batch            |
| `batch_item_id`                          | *str*                                    | :heavy_check_mark:                       | Unique identifier for an item in a batch |


### Response

**[operations.GetBulkCollaboratorBatchItemResponse](../../models/operations/getbulkcollaboratorbatchitemresponse.md)**


## update

Update a bulk collaborator batch item

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()


res = s.bulk_collaborator_batch_item.update(batch_id='occaecati', batch_item_id='numquam', bulk_collaborator_item_update=shared.BulkCollaboratorItemUpdate(
    collaborator_group_id='commodi',
    collaborator_id='quam',
    collaborator_status=shared.CollaboratorStatusBulkCollaboratorItemUpdate.INACTIVE,
    company='Mueller Inc',
    email='Bernie.Padberg@yahoo.com',
    external_id='odit',
    first_last_name='quo',
    form_w9_data=[],
    labels=[],
))

if res.bulk_collaborator_item is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `batch_id`                                                                                       | *str*                                                                                            | :heavy_check_mark:                                                                               | Unique identifier for a batch                                                                    |
| `batch_item_id`                                                                                  | *str*                                                                                            | :heavy_check_mark:                                                                               | Unique identifier for an item in a batch                                                         |
| `bulk_collaborator_item_update`                                                                  | [Optional[shared.BulkCollaboratorItemUpdate]](../../models/shared/bulkcollaboratoritemupdate.md) | :heavy_minus_sign:                                                                               | N/A                                                                                              |


### Response

**[operations.UpdateBulkCollaboratorBatchItemResponse](../../models/operations/updatebulkcollaboratorbatchitemresponse.md)**


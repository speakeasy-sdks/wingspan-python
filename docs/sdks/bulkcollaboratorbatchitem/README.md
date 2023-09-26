# BulkCollaboratorBatchItem

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


res = s.bulk_collaborator_batch_item.create(batch_id='id', bulk_collaborator_item_create=shared.BulkCollaboratorItemCreate(
    collaborator_group_id='possimus',
    collaborator_id='aut',
    collaborator_status=shared.CollaboratorStatusBulkCollaboratorItemCreate.ACTIVE,
    company='Smitham - Pacocha',
    email='Wanda.Wolf50@gmail.com',
    external_id='voluptatibus',
    first_last_name='ipsa',
    form_w9_data=shared.MemberClientFormW9Info(
        address_line1='voluptate',
        address_line2='cum',
        city='North Ilianaboro',
        company_structure=shared.CompanyStructureMemberClientFormW9Info.PARTNERSHIP,
        country='Brazil',
        dob='corporis',
        ein='dolore',
        first_name='Jayden',
        last_name='Carter',
        legal_business_name='harum',
        postal_code='84902',
        ssn='quidem',
        state='molestias',
    ),
    labels={
        "pariatur": 'modi',
    },
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


res = s.bulk_collaborator_batch_item.get(batch_id='praesentium', batch_item_id='rem')

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


res = s.bulk_collaborator_batch_item.update(batch_id='voluptates', batch_item_id='quasi', bulk_collaborator_item_update=shared.BulkCollaboratorItemUpdate(
    collaborator_group_id='repudiandae',
    collaborator_id='sint',
    collaborator_status=shared.CollaboratorStatusBulkCollaboratorItemUpdate.ACTIVE,
    company='Gottlieb, Hamill and Altenwerth',
    email='Roosevelt_Cole@hotmail.com',
    external_id='quibusdam',
    first_last_name='labore',
    form_w9_data='qui',
    labels='cupiditate',
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


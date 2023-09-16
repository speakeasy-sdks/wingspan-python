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


res = s.bulk_collaborator_batch_item.create(batch_id='enim', bulk_collaborator_item_create=shared.BulkCollaboratorItemCreate(
    collaborator_group_id='odit',
    collaborator_id='quo',
    collaborator_status=shared.CollaboratorStatusBulkCollaboratorItemCreate.ACTIVE,
    company='Hills, Ondricka and Schuster',
    email='Avery_Mueller9@gmail.com',
    external_id='reiciendis',
    first_last_name='voluptatibus',
    form_w9_data=shared.MemberClientFormW9Info(
        address_line1='nihil',
        address_line2='praesentium',
        city='Baltimore',
        company_structure=shared.CompanyStructureMemberClientFormW9Info.LLC_CORPORATION_C,
        country='Kazakhstan',
        dob='cum',
        ein='perferendis',
        first_name='Alison',
        last_name='Kiehn',
        legal_business_name='ut',
        postal_code='13241-6384',
        ssn='repudiandae',
        state='quae',
    ),
    labels='quidem',
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


res = s.bulk_collaborator_batch_item.get(batch_id='molestias', batch_item_id='excepturi')

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


res = s.bulk_collaborator_batch_item.update(batch_id='pariatur', batch_item_id='modi', bulk_collaborator_item_update=shared.BulkCollaboratorItemUpdate(
    collaborator_group_id='praesentium',
    collaborator_id='rem',
    collaborator_status=shared.CollaboratorStatusBulkCollaboratorItemUpdate.LESS_THAN_NIL_GREATER_THAN_,
    company='Waelchi LLC',
    email='Tobin0@gmail.com',
    external_id='est',
    first_last_name='quibusdam',
    form_w9_data='deserunt',
    labels={
        "quibusdam": 'labore',
    },
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


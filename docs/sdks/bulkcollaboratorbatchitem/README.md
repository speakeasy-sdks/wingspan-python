# bulk_collaborator_batch_item

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


res = s.bulk_collaborator_batch_item.create(batch_id='maiores', bulk_collaborator_item_create=shared.BulkCollaboratorItemCreate(
    collaborator_group_id='dicta',
    collaborator_id='corporis',
    collaborator_status=shared.CollaboratorStatusBulkCollaboratorItemCreate.INACTIVE,
    company='Carter - Pfeffer',
    email='Shania.Jerde21@gmail.com',
    external_id='quidem',
    first_last_name='molestias',
    form_w9_data=shared.MemberClientFormW9Info(
        address_line1='pariatur',
        address_line2='modi',
        city='Judahshire',
        company_structure=shared.CompanyStructureMemberClientFormW9Info.NONE,
        country='Turks and Caicos Islands',
        dob='sint',
        ein='veritatis',
        first_name='Tobin',
        last_name='Gottlieb',
        legal_business_name='enim',
        postal_code='68167',
        ssn='quibusdam',
        state='labore',
    ),
    labels='qui',
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


res = s.bulk_collaborator_batch_item.get(batch_id='aliquid', batch_item_id='cupiditate')

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


res = s.bulk_collaborator_batch_item.update(batch_id='quos', batch_item_id='perferendis', bulk_collaborator_item_update=shared.BulkCollaboratorItemUpdate(
    collaborator_group_id='magni',
    collaborator_id='assumenda',
    collaborator_status=shared.CollaboratorStatusBulkCollaboratorItemUpdate.INACTIVE,
    company='Corkery LLC',
    email='Dominique.Prosacco96@yahoo.com',
    external_id='eum',
    first_last_name='non',
    form_w9_data=shared.MemberClientFormW9Info(
        address_line1='sint',
        address_line2='aliquid',
        city='Sonyastead',
        company_structure=shared.CompanyStructureMemberClientFormW9Info.LLC_CORPORATION_C,
        country='Cyprus',
        dob='debitis',
        ein='a',
        first_name='Marilou',
        last_name='King',
        legal_business_name='in',
        postal_code='96127-8436',
        ssn='accusamus',
        state='non',
    ),
    labels={
        "accusamus": 'delectus',
        "quidem": 'provident',
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


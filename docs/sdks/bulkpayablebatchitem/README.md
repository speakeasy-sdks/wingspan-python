# BulkPayableBatchItem

### Available Operations

* [create](#create) - Create a bulk payable batch item
* [get](#get) - Get a bulk payable batch item
* [update](#update) - Update a bulk payable batch item

## create

Create a bulk payable batch item

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()


res = s.bulk_payable_batch_item.create(batch_id='nobis', bulk_payable_item_create=shared.BulkPayableItemCreate(
    amount=4287.69,
    attachment_id='vero',
    bulk_payable_batch_id='aspernatur',
    bulk_payable_item_merge_key='architecto',
    bulk_payable_item_reference='magnam',
    collaborator_email='et',
    collaborator_external_id='excepturi',
    collaborator_id='ullam',
    due_date='provident',
    labels={
        "sint": 'accusantium',
    },
    line_item_description='mollitia',
    line_item_detail='reiciendis',
    paid_date='mollitia',
    payable_notes='ad',
    payable_status=shared.PayableStatusBulkPayableItemCreate.APPROVED,
    reimbursable_expense='necessitatibus',
    workflow_sub_status=shared.WorkflowSubStatusBulkPayableItemCreate.SUBMITTED,
))

if res.bulk_payable_item is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `batch_id`                                                                             | *str*                                                                                  | :heavy_check_mark:                                                                     | Unique identifier for a batch                                                          |
| `bulk_payable_item_create`                                                             | [Optional[shared.BulkPayableItemCreate]](../../models/shared/bulkpayableitemcreate.md) | :heavy_minus_sign:                                                                     | N/A                                                                                    |


### Response

**[operations.CreateBulkPayableBatchItemResponse](../../models/operations/createbulkpayablebatchitemresponse.md)**


## get

Get a bulk payable batch item

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.bulk_payable_batch_item.get(batch_id='nemo', batch_item_id='quasi')

if res.bulk_payable_item is not None:
    # handle response
```

### Parameters

| Parameter                                | Type                                     | Required                                 | Description                              |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `batch_id`                               | *str*                                    | :heavy_check_mark:                       | Unique identifier for a batch            |
| `batch_item_id`                          | *str*                                    | :heavy_check_mark:                       | Unique identifier for an item in a batch |


### Response

**[operations.GetBulkPayableBatchItemResponse](../../models/operations/getbulkpayablebatchitemresponse.md)**


## update

Update a bulk payable batch item

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()


res = s.bulk_payable_batch_item.update(batch_id='iure', batch_item_id='doloribus', bulk_payable_item_update=shared.BulkPayableItemUpdate(
    amount=8919.24,
    attachment_id='eius',
    bulk_payable_batch_id='maxime',
    bulk_payable_item_merge_key='deleniti',
    bulk_payable_item_reference='facilis',
    collaborator_email='in',
    collaborator_external_id='architecto',
    collaborator_id='architecto',
    due_date='repudiandae',
    labels='expedita',
    line_item_description='nihil',
    line_item_detail='repellat',
    paid_date='quibusdam',
    payable_notes='sed',
    payable_status=shared.PayableStatusBulkPayableItemUpdate.LESS_THAN_NIL_GREATER_THAN_,
    reimbursable_expense=False,
    workflow_sub_status=shared.BulkPayableItemUpdateWorkflowSubStatus.SUBMITTED,
))

if res.bulk_payable_item is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `batch_id`                                                                             | *str*                                                                                  | :heavy_check_mark:                                                                     | Unique identifier for a batch                                                          |
| `batch_item_id`                                                                        | *str*                                                                                  | :heavy_check_mark:                                                                     | Unique identifier for an item in a batch                                               |
| `bulk_payable_item_update`                                                             | [Optional[shared.BulkPayableItemUpdate]](../../models/shared/bulkpayableitemupdate.md) | :heavy_minus_sign:                                                                     | N/A                                                                                    |


### Response

**[operations.UpdateBulkPayableBatchItemResponse](../../models/operations/updatebulkpayablebatchitemresponse.md)**


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


res = s.bulk_payable_batch_item.create(batch_id='et', bulk_payable_item_create=shared.BulkPayableItemCreate(
    amount=5699.65,
    attachment_id='ullam',
    bulk_payable_batch_id='provident',
    bulk_payable_item_merge_key='quos',
    bulk_payable_item_reference='sint',
    collaborator_email='accusantium',
    collaborator_external_id='mollitia',
    collaborator_id='reiciendis',
    due_date='mollitia',
    labels='eum',
    line_item_description='dolor',
    line_item_detail='necessitatibus',
    paid_date='odit',
    payable_notes='nemo',
    payable_status=shared.PayableStatusBulkPayableItemCreate.DRAFT,
    reimbursable_expense='doloribus',
    workflow_sub_status=shared.WorkflowSubStatusBulkPayableItemCreate.LESS_THAN_NIL_GREATER_THAN_,
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


res = s.bulk_payable_batch_item.get(batch_id='eius', batch_item_id='maxime')

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


res = s.bulk_payable_batch_item.update(batch_id='deleniti', batch_item_id='facilis', bulk_payable_item_update=shared.BulkPayableItemUpdate(
    amount=4479.26,
    attachment_id='architecto',
    bulk_payable_batch_id='architecto',
    bulk_payable_item_merge_key='repudiandae',
    bulk_payable_item_reference='ullam',
    collaborator_email='expedita',
    collaborator_external_id='nihil',
    collaborator_id='repellat',
    due_date='quibusdam',
    labels='saepe',
    line_item_description='pariatur',
    line_item_detail='accusantium',
    paid_date='consequuntur',
    payable_notes='praesentium',
    payable_status=shared.PayableStatusBulkPayableItemUpdate.PAID,
    reimbursable_expense='sunt',
    workflow_sub_status=shared.BulkPayableItemUpdateWorkflowSubStatus.LESS_THAN_NIL_GREATER_THAN_,
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


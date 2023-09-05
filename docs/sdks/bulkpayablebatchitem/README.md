# bulk_payable_batch_item

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


res = s.bulk_payable_batch_item.create(batch_id='cumque', bulk_payable_item_create=shared.BulkPayableItemCreate(
    amount=3599.78,
    attachment_id='hic',
    bulk_payable_batch_id='libero',
    bulk_payable_item_merge_key='nobis',
    bulk_payable_item_reference='dolores',
    collaborator_email='quis',
    collaborator_external_id='totam',
    collaborator_id='dignissimos',
    due_date='eaque',
    labels='nesciunt',
    line_item_description='eos',
    line_item_detail='perferendis',
    paid_date='dolores',
    payable_notes='minus',
    payable_status=shared.PayableStatusBulkPayableItemCreate.APPROVED,
    reimbursable_expense='vero',
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


res = s.bulk_payable_batch_item.get(batch_id='hic', batch_item_id='recusandae')

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


res = s.bulk_payable_batch_item.update(batch_id='omnis', batch_item_id='facilis', bulk_payable_item_update=shared.BulkPayableItemUpdate(
    amount=5966.56,
    attachment_id='voluptatem',
    bulk_payable_batch_id='porro',
    bulk_payable_item_merge_key='consequuntur',
    bulk_payable_item_reference='blanditiis',
    collaborator_email='error',
    collaborator_external_id='eaque',
    collaborator_id='occaecati',
    due_date='rerum',
    labels='asperiores',
    line_item_description='earum',
    line_item_detail='modi',
    paid_date='iste',
    payable_notes='dolorum',
    payable_status=shared.PayableStatusBulkPayableItemUpdate.PAID,
    reimbursable_expense=False,
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


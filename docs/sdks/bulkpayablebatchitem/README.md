# BulkPayableBatchItem
(*bulk_payable_batch_item*)

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


res = s.bulk_payable_batch_item.create(batch_id='sint', bulk_payable_item_create=shared.BulkPayableItemCreate(
    amount=831.12,
    attachment_id='itaque',
    bulk_payable_batch_id='incidunt',
    bulk_payable_item_merge_key='enim',
    bulk_payable_item_reference='consequatur',
    collaborator_email='est',
    collaborator_external_id='quibusdam',
    collaborator_id='explicabo',
    due_date='deserunt',
    labels=[],
    line_item_description='distinctio',
    line_item_detail='quibusdam',
    paid_date='labore',
    payable_notes='modi',
    payable_status=shared.PayableStatusBulkPayableItemCreate.DRAFT,
    reimbursable_expense=[],
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


res = s.bulk_payable_batch_item.get(batch_id='cupiditate', batch_item_id='quos')

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


res = s.bulk_payable_batch_item.update(batch_id='perferendis', batch_item_id='magni', bulk_payable_item_update=shared.BulkPayableItemUpdate(
    amount=8289.4,
    attachment_id='ipsam',
    bulk_payable_batch_id='alias',
    bulk_payable_item_merge_key='fugit',
    bulk_payable_item_reference='dolorum',
    collaborator_email='excepturi',
    collaborator_external_id='tempora',
    collaborator_id='facilis',
    due_date='tempore',
    labels=[],
    line_item_description='labore',
    line_item_detail='delectus',
    paid_date='eum',
    payable_notes='non',
    payable_status=shared.PayableStatusBulkPayableItemUpdate.CANCELLED,
    reimbursable_expense=[],
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


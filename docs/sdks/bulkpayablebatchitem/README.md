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


res = s.bulk_payable_batch_item.create(batch_id='online', bulk_payable_item_create=shared.BulkPayableItemCreate(
    amount=6384.24,
    attachment_id='Money blue shred',
    bulk_payable_batch_id='technology East',
    bulk_payable_item_merge_key='evolve',
    bulk_payable_item_reference='fuchsia Gasoline Screen',
    collaborator_email='physical Ameliorated',
    collaborator_external_id='after',
    collaborator_id='Intelligent Fish',
    due_date='Fiat',
    labels=[],
    line_item_description='Grocery Borders Northwest',
    line_item_detail='Kentucky animated',
    paid_date='Interactions Senior Mouse',
    payable_notes='or',
    payable_status=shared.PayableStatusBulkPayableItemCreate.OPEN,
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


res = s.bulk_payable_batch_item.get(batch_id='female', batch_item_id='program')

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


res = s.bulk_payable_batch_item.update(batch_id='Van', batch_item_id='East', bulk_payable_item_update=shared.BulkPayableItemUpdate(
    amount=7084.55,
    attachment_id='Metal cheater Islands',
    bulk_payable_batch_id='withdrawal extend',
    bulk_payable_item_merge_key='bifurcated',
    bulk_payable_item_reference='silver immediately',
    collaborator_email='East',
    collaborator_external_id='Bicycle guestbook',
    collaborator_id='Galveston pascal',
    due_date='Division Northeast Wooden',
    labels=[],
    line_item_description='Jaguar Dodge',
    line_item_detail='Buckinghamshire frictionless haptic',
    paid_date='possimus navigating Diesel',
    payable_notes='Greens',
    payable_status=shared.PayableStatusBulkPayableItemUpdate.PAID,
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


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
from wingspan.models import shared

s = wingspan.Wingspan()


res = s.bulk_payable_batch_item.create(batch_id='<value>', bulk_payable_item_create=shared.BulkPayableItemCreate(
    amount=4865.89,
    bulk_payable_batch_id='<value>',
    due_date='<value>',
    line_item_description='<value>',
    payable_status=shared.PayableStatusBulkPayableItemCreate.APPROVED,
))

if res.bulk_payable_item is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `batch_id`                                                                             | *str*                                                                                  | :heavy_check_mark:                                                                     | Unique identifier for a batch                                                          |
| `bulk_payable_item_create`                                                             | [Optional[shared.BulkPayableItemCreate]](../../models/shared/bulkpayableitemcreate.md) | :heavy_minus_sign:                                                                     | N/A                                                                                    |


### Response

**[operations.CreateBulkPayableBatchItemResponse](../../models/operations/createbulkpayablebatchitemresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get

Get a bulk payable batch item

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.bulk_payable_batch_item.get(batch_id='<value>', batch_item_id='<value>')

if res.bulk_payable_item is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                | Type                                     | Required                                 | Description                              |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `batch_id`                               | *str*                                    | :heavy_check_mark:                       | Unique identifier for a batch            |
| `batch_item_id`                          | *str*                                    | :heavy_check_mark:                       | Unique identifier for an item in a batch |


### Response

**[operations.GetBulkPayableBatchItemResponse](../../models/operations/getbulkpayablebatchitemresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update

Update a bulk payable batch item

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()


res = s.bulk_payable_batch_item.update(batch_id='<value>', batch_item_id='<value>', bulk_payable_item_update=shared.BulkPayableItemUpdate())

if res.bulk_payable_item is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `batch_id`                                                                             | *str*                                                                                  | :heavy_check_mark:                                                                     | Unique identifier for a batch                                                          |
| `batch_item_id`                                                                        | *str*                                                                                  | :heavy_check_mark:                                                                     | Unique identifier for an item in a batch                                               |
| `bulk_payable_item_update`                                                             | [Optional[shared.BulkPayableItemUpdate]](../../models/shared/bulkpayableitemupdate.md) | :heavy_minus_sign:                                                                     | N/A                                                                                    |


### Response

**[operations.UpdateBulkPayableBatchItemResponse](../../models/operations/updatebulkpayablebatchitemresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

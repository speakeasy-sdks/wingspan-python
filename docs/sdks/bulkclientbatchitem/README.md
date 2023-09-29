# BulkClientBatchItem
(*bulk_client_batch_item*)

### Available Operations

* [create](#create) - Create a bulk client batch item
* [get](#get) - Get a bulk client batch item
* [update](#update) - Update a bulk client batch item

## create

Create a bulk client batch item

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()


res = s.bulk_client_batch_item.create(batch_id='online', bulk_client_item_create=shared.BulkClientItemCreate(
    client_status=shared.ClientStatusBulkClientItemCreate.PENDING,
    company='Johnson, Green and Collier',
    email='Annie.Zieme95@hotmail.com',
    external_id='East orange Northwest',
    first_last_name='SUV quantify Polestar',
    integration=[],
    labels=[],
    member_data=[],
))

if res.bulk_client_item is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `batch_id`                                                                           | *str*                                                                                | :heavy_check_mark:                                                                   | Unique identifier for a batch                                                        |
| `bulk_client_item_create`                                                            | [Optional[shared.BulkClientItemCreate]](../../models/shared/bulkclientitemcreate.md) | :heavy_minus_sign:                                                                   | N/A                                                                                  |


### Response

**[operations.CreateBulkClientBatchItemResponse](../../models/operations/createbulkclientbatchitemresponse.md)**


## get

Get a bulk client batch item

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.bulk_client_batch_item.get(batch_id='female', batch_item_id='program')

if res.bulk_client_item is not None:
    # handle response
```

### Parameters

| Parameter                                | Type                                     | Required                                 | Description                              |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `batch_id`                               | *str*                                    | :heavy_check_mark:                       | Unique identifier for a batch            |
| `batch_item_id`                          | *str*                                    | :heavy_check_mark:                       | Unique identifier for an item in a batch |


### Response

**[operations.GetBulkClientBatchItemResponse](../../models/operations/getbulkclientbatchitemresponse.md)**


## update

Update a bulk client batch item

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()


res = s.bulk_client_batch_item.update(batch_id='Van', batch_item_id='East', bulk_client_item_update=shared.BulkClientItemUpdate(
    client_status=shared.ClientStatusBulkClientItemUpdate.PENDING,
    company='Glover, Murazik and Paucek',
    email='Immanuel5@yahoo.com',
    external_id='mostly',
    first_last_name='dynamic white',
    integration=[],
    labels=[],
    member_data=[],
))

if res.bulk_client_item is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `batch_id`                                                                           | *str*                                                                                | :heavy_check_mark:                                                                   | Unique identifier for a batch                                                        |
| `batch_item_id`                                                                      | *str*                                                                                | :heavy_check_mark:                                                                   | Unique identifier for an item in a batch                                             |
| `bulk_client_item_update`                                                            | [Optional[shared.BulkClientItemUpdate]](../../models/shared/bulkclientitemupdate.md) | :heavy_minus_sign:                                                                   | N/A                                                                                  |


### Response

**[operations.UpdateBulkClientBatchItemResponse](../../models/operations/updatebulkclientbatchitemresponse.md)**


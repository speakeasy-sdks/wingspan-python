# BulkClientBatchItem

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


res = s.bulk_client_batch_item.create(batch_id='fuga', bulk_client_item_create=shared.BulkClientItemCreate(
    client_status=shared.ClientStatusBulkClientItemCreate.INACTIVE,
    company='Moore - Kertzmann',
    email='Maxie96@hotmail.com',
    external_id='est',
    first_last_name='mollitia',
    integration=shared.D750b2d9403b5bcbdb3c96c89f1cc713df563d587f16e5f39f5ab546c08a20a0(
        quickbooks='dolorem',
    ),
    labels='explicabo',
    member_data=shared.MemberData(
        auto_pay_requirement=shared.AutoPayRequirementMemberData.ALL,
        external_id='omnis',
        share_tax_document=shared.ShareTaxDocumentMemberData.DECLINE,
    ),
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


res = s.bulk_client_batch_item.get(batch_id='minima', batch_item_id='excepturi')

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


res = s.bulk_client_batch_item.update(batch_id='accusantium', batch_item_id='iure', bulk_client_item_update=shared.BulkClientItemUpdate(
    client_status=shared.ClientStatusBulkClientItemUpdate.PENDING,
    company='Williamson, Brakus and O'Hara',
    email='Lorine_Crooks58@gmail.com',
    external_id='numquam',
    first_last_name='commodi',
    integration='molestiae',
    labels='error',
    member_data='quis',
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


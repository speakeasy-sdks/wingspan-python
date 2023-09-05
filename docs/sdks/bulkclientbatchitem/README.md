# bulk_client_batch_item

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


res = s.bulk_client_batch_item.create(batch_id='architecto', bulk_client_item_create=shared.BulkClientItemCreate(
    client_status=shared.ClientStatusBulkClientItemCreate.ACTIVE,
    company='Orn, O'Hara and Osinski',
    email='Corrine75@gmail.com',
    external_id='enim',
    first_last_name='omnis',
    integration='minima',
    labels={
        "iure": 'culpa',
    },
    member_data=shared.MemberData(
        auto_pay_requirement=shared.AutoPayRequirementMemberData.LESS_THAN_NIL_GREATER_THAN_,
        external_id='architecto',
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


res = s.bulk_client_batch_item.get(batch_id='dolorem', batch_item_id='culpa')

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


res = s.bulk_client_batch_item.update(batch_id='consequuntur', batch_item_id='repellat', bulk_client_item_update=shared.BulkClientItemUpdate(
    client_status=shared.ClientStatusBulkClientItemUpdate.PENDING,
    company='Fritsch - Jerde',
    email='Jarred.Frami@yahoo.com',
    external_id='quis',
    first_last_name='vitae',
    integration=shared.D750b2d9403b5bcbdb3c96c89f1cc713df563d587f16e5f39f5ab546c08a20a0(
        quickbooks=shared.SixtyFourMillionEightHundredAndFortySixThousandOneHundredAndThirtySixa354aa510825c1f23c3a978f4c816d8d4184311e7294a570f73727dc(
            customer_id='enim',
            item_id='odit',
        ),
    ),
    labels={
        "tenetur": 'ipsam',
    },
    member_data=shared.MemberData(
        auto_pay_requirement=shared.AutoPayRequirementMemberData.LESS_THAN_NIL_GREATER_THAN_,
        external_id='aut',
        share_tax_document=shared.ShareTaxDocumentMemberData.ALLOW,
    ),
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


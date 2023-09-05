# bulk_calculation1099_batch_item

### Available Operations

* [create](#create) - Create a bulk calculation1099 batch item
* [get](#get) - Get a bulk calculation1099 batch item
* [update](#update) - Update a bulk calculation1099 batch item

## create

Create a bulk calculation1099 batch item

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()


res = s.bulk_calculation1099_batch_item.create(batch_id='totam', bulk_calculation1099_item_create=shared.BulkCalculation1099ItemCreate(
    calculation_type=shared.CalculationTypeBulkCalculation1099ItemCreate.BALANCES,
    client_id='commodi',
    labels='modi',
    year=1863.32,
))

if res.bulk_calculation1099_item is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `batch_id`                                                                                             | *str*                                                                                                  | :heavy_check_mark:                                                                                     | Unique identifier for a batch                                                                          |
| `bulk_calculation1099_item_create`                                                                     | [Optional[shared.BulkCalculation1099ItemCreate]](../../models/shared/bulkcalculation1099itemcreate.md) | :heavy_minus_sign:                                                                                     | N/A                                                                                                    |


### Response

**[operations.CreateBulkCalculation1099BatchItemResponse](../../models/operations/createbulkcalculation1099batchitemresponse.md)**


## get

Get a bulk calculation1099 batch item

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.bulk_calculation1099_batch_item.get(batch_id='impedit', batch_item_id='cum')

if res.bulk_calculation1099_item is not None:
    # handle response
```

### Parameters

| Parameter                                | Type                                     | Required                                 | Description                              |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `batch_id`                               | *str*                                    | :heavy_check_mark:                       | Unique identifier for a batch            |
| `batch_item_id`                          | *str*                                    | :heavy_check_mark:                       | Unique identifier for an item in a batch |


### Response

**[operations.GetBulkCalculation1099BatchItemResponse](../../models/operations/getbulkcalculation1099batchitemresponse.md)**


## update

Update a bulk calculation1099 batch item

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()


res = s.bulk_calculation1099_batch_item.update(batch_id='esse', batch_item_id='ipsum', bulk_calculation1099_item_update=shared.BulkCalculation1099ItemUpdate(
    calculation_type=shared.CalculationTypeBulkCalculation1099ItemUpdate.SUBMISSIONS,
    client_id='aspernatur',
    labels='ad',
    year=6176.36,
))

if res.bulk_payable_item is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `batch_id`                                                                                             | *str*                                                                                                  | :heavy_check_mark:                                                                                     | Unique identifier for a batch                                                                          |
| `batch_item_id`                                                                                        | *str*                                                                                                  | :heavy_check_mark:                                                                                     | Unique identifier for an item in a batch                                                               |
| `bulk_calculation1099_item_update`                                                                     | [Optional[shared.BulkCalculation1099ItemUpdate]](../../models/shared/bulkcalculation1099itemupdate.md) | :heavy_minus_sign:                                                                                     | N/A                                                                                                    |


### Response

**[operations.UpdateBulkCalculation1099BatchItemResponse](../../models/operations/updatebulkcalculation1099batchitemresponse.md)**

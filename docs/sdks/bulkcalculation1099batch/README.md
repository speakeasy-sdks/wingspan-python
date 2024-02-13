# BulkCalculation1099Batch
(*bulk_calculation1099_batch*)

### Available Operations

* [create](#create) - Create a bulk calculation1099 batch
* [get](#get) - Get a bulk calculation1099 batch
* [update](#update) - Update a bulk calculation1099 batch

## create

Create a bulk calculation1099 batch

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()

req = shared.BulkBatchCreate()

res = s.bulk_calculation1099_batch.create(req)

if res.bulk_calculation1099_batch is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                        | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `request`                                                        | [shared.BulkBatchCreate](../../models/shared/bulkbatchcreate.md) | :heavy_check_mark:                                               | The request object to use for the request.                       |


### Response

**[operations.CreateBulkCalculation1099BatchResponse](../../models/operations/createbulkcalculation1099batchresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get

Get a bulk calculation1099 batch

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.bulk_calculation1099_batch.get(batch_id='string')

if res.bulk_calculation1099_batch is not None:
    # handle response
    pass
```

### Parameters

| Parameter                     | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `batch_id`                    | *str*                         | :heavy_check_mark:            | Unique identifier for a batch |


### Response

**[operations.GetBulkCalculation1099BatchResponse](../../models/operations/getbulkcalculation1099batchresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update

Update a bulk calculation1099 batch

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()


res = s.bulk_calculation1099_batch.update(batch_id='string', bulk_batch_update=shared.BulkBatchUpdate())

if res.bulk_calculation1099_batch is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `batch_id`                                                                 | *str*                                                                      | :heavy_check_mark:                                                         | Unique identifier for a batch                                              |
| `bulk_batch_update`                                                        | [Optional[shared.BulkBatchUpdate]](../../models/shared/bulkbatchupdate.md) | :heavy_minus_sign:                                                         | N/A                                                                        |


### Response

**[operations.UpdateBulkCalculation1099BatchResponse](../../models/operations/updatebulkcalculation1099batchresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

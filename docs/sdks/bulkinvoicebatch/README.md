# BulkInvoiceBatch
(*bulk_invoice_batch*)

### Available Operations

* [create](#create) - Create a bulk invoice batch
* [get](#get) - Get a bulk invoice batch
* [update](#update) - Update a bulk invoice batch

## create

Create a bulk invoice batch

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()

req = shared.BulkInvoiceBatchCreate(
    labels={
        "key": 'string',
    },
    processing_strategy=shared.BulkInvoiceBatchCreateProcessingStrategy.MERGE,
)

res = s.bulk_invoice_batch.create(req)

if res.bulk_invoice_batch is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.BulkInvoiceBatchCreate](../../models/shared/bulkinvoicebatchcreate.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.CreateBulkInvoiceBatchResponse](../../models/operations/createbulkinvoicebatchresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get

Get a bulk invoice batch

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.bulk_invoice_batch.get(batch_id='string')

if res.bulk_invoice_batch is not None:
    # handle response
    pass
```

### Parameters

| Parameter                     | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `batch_id`                    | *str*                         | :heavy_check_mark:            | Unique identifier for a batch |


### Response

**[operations.GetBulkInvoiceBatchResponse](../../models/operations/getbulkinvoicebatchresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## update

Update a bulk invoice batch

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()


res = s.bulk_invoice_batch.update(batch_id='string', bulk_invoice_batch_update=shared.BulkInvoiceBatchUpdate(
    labels={
        "key": 'string',
    },
))

if res.bulk_invoice_batch is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `batch_id`                                                                               | *str*                                                                                    | :heavy_check_mark:                                                                       | Unique identifier for a batch                                                            |
| `bulk_invoice_batch_update`                                                              | [Optional[shared.BulkInvoiceBatchUpdate]](../../models/shared/bulkinvoicebatchupdate.md) | :heavy_minus_sign:                                                                       | N/A                                                                                      |


### Response

**[operations.UpdateBulkInvoiceBatchResponse](../../models/operations/updatebulkinvoicebatchresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

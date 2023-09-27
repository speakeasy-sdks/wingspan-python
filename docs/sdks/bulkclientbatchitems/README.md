# BulkClientBatchItems
(*bulk_client_batch_items*)

### Available Operations

* [list](#list) - List bulk client batch items

## list

List bulk client batch items

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.bulk_client_batch_items.list(batch_id='corporis')

if res.bulk_client_items is not None:
    # handle response
```

### Parameters

| Parameter                     | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `batch_id`                    | *str*                         | :heavy_check_mark:            | Unique identifier for a batch |


### Response

**[operations.ListBulkClientBatchItemsResponse](../../models/operations/listbulkclientbatchitemsresponse.md)**


# BulkPayableBatchItems
(*bulk_payable_batch_items*)

### Available Operations

* [list](#list) - List bulk payable batch items

## list

List bulk payable batch items

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.bulk_payable_batch_items.list(batch_id='Bicycle')

if res.bulk_payable_items is not None:
    # handle response
    pass
```

### Parameters

| Parameter                     | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `batch_id`                    | *str*                         | :heavy_check_mark:            | Unique identifier for a batch |


### Response

**[operations.ListBulkPayableBatchItemsResponse](../../models/operations/listbulkpayablebatchitemsresponse.md)**


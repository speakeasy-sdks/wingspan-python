# bulk_calculation1099_batch_items

### Available Operations

* [list](#list) - List bulk calculation1099 batch items

## list

List bulk calculation1099 batch items

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.bulk_calculation1099_batch_items.list(batch_id='esse')

if res.bulk_calculation1099_items is not None:
    # handle response
```

### Parameters

| Parameter                     | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `batch_id`                    | *str*                         | :heavy_check_mark:            | Unique identifier for a batch |


### Response

**[operations.ListBulkCalculation1099BatchItemsResponse](../../models/operations/listbulkcalculation1099batchitemsresponse.md)**


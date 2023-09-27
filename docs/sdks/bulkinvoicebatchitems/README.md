# BulkInvoiceBatchItems
(*bulk_invoice_batch_items*)

### Available Operations

* [list](#list) - List bulk invoice batch items

## list

List bulk invoice batch items

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.bulk_invoice_batch_items.list(batch_id='modi')

if res.bulk_invoice_items is not None:
    # handle response
```

### Parameters

| Parameter                     | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `batch_id`                    | *str*                         | :heavy_check_mark:            | Unique identifier for a batch |


### Response

**[operations.ListBulkInvoiceBatchItemsResponse](../../models/operations/listbulkinvoicebatchitemsresponse.md)**


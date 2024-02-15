# BulkInvoiceBatchItems
(*bulk_invoice_batch_items*)

### Available Operations

* [list](#list) - List bulk invoice batch items

## list

List bulk invoice batch items

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.bulk_invoice_batch_items.list(batch_id='<value>')

if res.classes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                     | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `batch_id`                    | *str*                         | :heavy_check_mark:            | Unique identifier for a batch |


### Response

**[operations.ListBulkInvoiceBatchItemsResponse](../../models/operations/listbulkinvoicebatchitemsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

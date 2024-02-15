# BulkClientBatchItems
(*bulk_client_batch_items*)

### Available Operations

* [list](#list) - List bulk client batch items

## list

List bulk client batch items

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.bulk_client_batch_items.list(batch_id='<value>')

if res.classes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                     | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `batch_id`                    | *str*                         | :heavy_check_mark:            | Unique identifier for a batch |


### Response

**[operations.ListBulkClientBatchItemsResponse](../../models/operations/listbulkclientbatchitemsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

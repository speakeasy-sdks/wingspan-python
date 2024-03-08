# BulkCollaboratorBatchItems
(*bulk_collaborator_batch_items*)

### Available Operations

* [list](#list) - List bulk collaborator batch items

## list

List bulk collaborator batch items

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.bulk_collaborator_batch_items.list(batch_id='<value>')

if res.classes is not None:
    # handle response
    pass

```

### Parameters

| Parameter                     | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `batch_id`                    | *str*                         | :heavy_check_mark:            | Unique identifier for a batch |


### Response

**[operations.ListBulkCollaboratorBatchItemsResponse](../../models/operations/listbulkcollaboratorbatchitemsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

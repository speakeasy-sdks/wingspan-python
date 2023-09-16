# BulkClientBatches

### Available Operations

* [list](#list) - List bulk client batches

## list

List bulk client batches

### Example Usage

```python
import wingspan


s = wingspan.Wingspan()


res = s.bulk_client_batches.list()

if res.bulk_client_batches is not None:
    # handle response
```


### Response

**[operations.ListBulkClientBatchesResponse](../../models/operations/listbulkclientbatchesresponse.md)**


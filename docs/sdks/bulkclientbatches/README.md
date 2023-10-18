# BulkClientBatches
(*bulk_client_batches*)

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
    pass
```


### Response

**[operations.ListBulkClientBatchesResponse](../../models/operations/listbulkclientbatchesresponse.md)**


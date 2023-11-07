# BulkCollaboratorBatches
(*.bulk_collaborator_batches*)

### Available Operations

* [list](#list) - List bulk collaborator batches

## list

List bulk collaborator batches

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.bulk_collaborator_batches.list()

if res.classes is not None:
    # handle response
    pass
```


### Response

**[operations.ListBulkCollaboratorBatchesResponse](../../models/operations/listbulkcollaboratorbatchesresponse.md)**


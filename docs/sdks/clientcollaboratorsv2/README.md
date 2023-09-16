# ClientCollaboratorsV2

### Available Operations

* [list](#list) - Lists all collaborators in the V2 format

## list

Lists all collaborators in the V2 format

### Example Usage

```python
import wingspan


s = wingspan.Wingspan()


res = s.client_collaborators_v2.list()

if res.collaborator_v2s is not None:
    # handle response
```


### Response

**[operations.ListClientCollaboratorsV2Response](../../models/operations/listclientcollaboratorsv2response.md)**


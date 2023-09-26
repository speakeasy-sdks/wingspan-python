# Collaborators

### Available Operations

* [list](#list) - List all collaborators

## list

List all collaborators

### Example Usage

```python
import wingspan


s = wingspan.Wingspan()


res = s.collaborators.list()

if res.collaborator_schemas is not None:
    # handle response
```


### Response

**[operations.ListCollaboratorsResponse](../../models/operations/listcollaboratorsresponse.md)**


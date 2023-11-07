# CollaboratorGroups
(*.collaborator_groups*)

### Available Operations

* [list](#list) - List Collaborator Groups

## list

List Collaborator Groups

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.collaborator_groups.list()

if res.classes is not None:
    # handle response
    pass
```


### Response

**[operations.ListCollaboratorGroupsResponse](../../models/operations/listcollaboratorgroupsresponse.md)**


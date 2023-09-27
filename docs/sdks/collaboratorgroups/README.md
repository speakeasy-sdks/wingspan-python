# CollaboratorGroups
(*collaborator_groups*)

### Available Operations

* [list](#list) - List Collaborator Groups

## list

List Collaborator Groups

### Example Usage

```python
import wingspan


s = wingspan.Wingspan()


res = s.collaborator_groups.list()

if res.collaborator_group_responses is not None:
    # handle response
```


### Response

**[operations.ListCollaboratorGroupsResponse](../../models/operations/listcollaboratorgroupsresponse.md)**


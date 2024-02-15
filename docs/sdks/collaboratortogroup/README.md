# CollaboratorToGroup
(*collaborator_to_group*)

### Available Operations

* [add](#add) - Add collaborator to collaborators group
* [remove](#remove) - Remove collaborator from collaborators group

## add

Add collaborator to collaborators group

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.collaborator_to_group.add(group_id='<value>', id='<value>')

if res.collaborator_schema is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `group_id`         | *str*              | :heavy_check_mark: | Unique group Id    |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.AddCollaboratorToGroupResponse](../../models/operations/addcollaboratortogroupresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove

Remove collaborator from collaborators group

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.collaborator_to_group.remove(group_id='<value>', id='<value>')

if res.collaborator_schema is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `group_id`         | *str*              | :heavy_check_mark: | Unique group Id    |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.RemoveCollaboratorToGroupResponse](../../models/operations/removecollaboratortogroupresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

# collaborator_to_group

### Available Operations

* [add](#add) - Add collaborator to collaborators group
* [remove](#remove) - Remove collaborator from collaborators group

## add

Add collaborator to collaborators group

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.collaborator_to_group.add(group_id='dolores', id='distinctio')

if res.collaborator_schema is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `group_id`         | *str*              | :heavy_check_mark: | Unique group Id    |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.AddCollaboratorToGroupResponse](../../models/operations/addcollaboratortogroupresponse.md)**


## remove

Remove collaborator from collaborators group

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.collaborator_to_group.remove(group_id='facilis', id='aliquid')

if res.collaborator_schema is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `group_id`         | *str*              | :heavy_check_mark: | Unique group Id    |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.RemoveCollaboratorToGroupResponse](../../models/operations/removecollaboratortogroupresponse.md)**


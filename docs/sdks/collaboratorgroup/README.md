# CollaboratorGroup
(*collaborator_group*)

### Available Operations

* [create](#create) - Create Collaborator Group
* [get](#get) - Get Collaborator Group
* [update](#update) - Update Collaborator Group

## create

Create Collaborator Group

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()

req = shared.CollaboratorGroupCreateRequest(
    description='Multi-tiered human-resource model',
    name='string',
)

res = s.collaborator_group.create(req)

if res.collaborator_group_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [shared.CollaboratorGroupCreateRequest](../../models/shared/collaboratorgroupcreaterequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.CreateCollaboratorGroupResponse](../../models/operations/createcollaboratorgroupresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get

Get Collaborator Group

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.collaborator_group.get(id='string')

if res.collaborator_group_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.GetCollaboratorGroupResponse](../../models/operations/getcollaboratorgroupresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update

Update Collaborator Group

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()


res = s.collaborator_group.update(id='string', collaborator_group_update_request=shared.CollaboratorGroupUpdateRequest())

if res.collaborator_group_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                     | *str*                                                                                                    | :heavy_check_mark:                                                                                       | Unique identifier                                                                                        |
| `collaborator_group_update_request`                                                                      | [Optional[shared.CollaboratorGroupUpdateRequest]](../../models/shared/collaboratorgroupupdaterequest.md) | :heavy_minus_sign:                                                                                       | N/A                                                                                                      |


### Response

**[operations.UpdateCollaboratorGroupResponse](../../models/operations/updatecollaboratorgroupresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

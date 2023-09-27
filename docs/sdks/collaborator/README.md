# Collaborator
(*collaborator*)

### Available Operations

* [create](#create) - Create new collaborator
* [delete](#delete) - Delete collaborator by Id
* [get](#get) - Get collaborator by Id
* [update](#update) - Update a collaborator by Id

## create

Create new collaborator

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()

req = shared.CollaboratorCreateRequest(
    client_data=[],
    client_id='nemo',
    collaborator_group_id='quasi',
    form_w9_data=[],
    integration=[],
    labels=[],
    member_company='iure',
    member_email='doloribus',
    member_id='debitis',
    member_name='eius',
    status=shared.StatusCollaboratorCreateRequest.LESS_THAN_NIL_GREATER_THAN_,
)

res = s.collaborator.create(req)

if res.collaborator_schema is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [shared.CollaboratorCreateRequest](../../models/shared/collaboratorcreaterequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.CreateCollaboratorResponse](../../models/operations/createcollaboratorresponse.md)**


## delete

Delete collaborator by Id

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.collaborator.delete(id='deleniti')

if res.collaborator_schema is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.DeleteCollaboratorResponse](../../models/operations/deletecollaboratorresponse.md)**


## get

Get collaborator by Id

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.collaborator.get(id='facilis')

if res.collaborator_schema is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.GetCollaboratorResponse](../../models/operations/getcollaboratorresponse.md)**


## update

Update a collaborator by Id

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()


res = s.collaborator.update(id='in', collaborator_update_request=shared.CollaboratorUpdateRequest(
    client_data=[],
    form1099_balances=[],
    form_w9_data=[],
    integration=[],
    labels=[],
    status=shared.StatusCollaboratorUpdateRequest.ACTIVE,
))

if res.collaborator_schema is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `id`                                                                                           | *str*                                                                                          | :heavy_check_mark:                                                                             | Unique identifier                                                                              |
| `collaborator_update_request`                                                                  | [Optional[shared.CollaboratorUpdateRequest]](../../models/shared/collaboratorupdaterequest.md) | :heavy_minus_sign:                                                                             | N/A                                                                                            |


### Response

**[operations.UpdateCollaboratorResponse](../../models/operations/updatecollaboratorresponse.md)**


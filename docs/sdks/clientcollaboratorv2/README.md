# client_collaborator_v2

### Available Operations

* [get](#get) - Get a single V2 Collaborator by clientId

## get

Get a single V2 Collaborator by clientId

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.client_collaborator_v2.get(client_id='qui')

if res.collaborator_v2 is not None:
    # handle response
```

### Parameters

| Parameter                     | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `client_id`                   | *str*                         | :heavy_check_mark:            | Unique identifier of a client |


### Response

**[operations.GetClientCollaboratorV2Response](../../models/operations/getclientcollaboratorv2response.md)**


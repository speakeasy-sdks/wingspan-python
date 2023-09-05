# collaborator_v2

### Available Operations

* [get](#get) - Get a single V2 Collaborator by memberId

## get

Get a single V2 Collaborator by memberId

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.collaborator_v2.get(member_id='ipsa')

if res.collaborator_v2 is not None:
    # handle response
```

### Parameters

| Parameter                     | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `member_id`                   | *str*                         | :heavy_check_mark:            | Unique identifier of a member |


### Response

**[operations.GetCollaboratorV2Response](../../models/operations/getcollaboratorv2response.md)**


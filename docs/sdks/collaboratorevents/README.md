# CollaboratorEvents
(*collaborator_events*)

### Available Operations

* [get](#get) - Get collaborator events by collaboratorId

## get

Get collaborator events by collaboratorId

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.collaborator_events.get(id='quidem')

if res.collaborator_events is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.GetCollaboratorEventsResponse](../../models/operations/getcollaboratoreventsresponse.md)**


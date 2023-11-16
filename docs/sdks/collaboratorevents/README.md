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


res = s.collaborator_events.get(id='string')

if res.collaborator_events is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.GetCollaboratorEventsResponse](../../models/operations/getcollaboratoreventsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

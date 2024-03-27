# ClientCollaboratorV2
(*client_collaborator_v2*)

### Available Operations

* [get](#get) - Get a single V2 Collaborator by clientId

## get

Get a single V2 Collaborator by clientId

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.client_collaborator_v2.get(client_id='<value>')

if res.collaborator_v2 is not None:
    # handle response
    pass

```

### Parameters

| Parameter                     | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `client_id`                   | *str*                         | :heavy_check_mark:            | Unique identifier of a client |


### Response

**[operations.GetClientCollaboratorV2Response](../../models/operations/getclientcollaboratorv2response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

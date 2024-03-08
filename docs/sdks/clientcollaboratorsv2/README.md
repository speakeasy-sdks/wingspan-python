# ClientCollaboratorsV2
(*client_collaborators_v2*)

### Available Operations

* [list](#list) - Lists all collaborators in the V2 format

## list

Lists all collaborators in the V2 format

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.client_collaborators_v2.list()

if res.classes is not None:
    # handle response
    pass

```


### Response

**[operations.ListClientCollaboratorsV2Response](../../models/operations/listclientcollaboratorsv2response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

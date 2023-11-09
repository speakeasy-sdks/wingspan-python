# CollaboratorsV2
(*collaborators_v2*)

### Available Operations

* [list](#list) - Lists all collaborators in the V2 format

## list

Lists all collaborators in the V2 format

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.collaborators_v2.list()

if res.classes is not None:
    # handle response
    pass
```


### Response

**[operations.ListCollaboratorsV2Response](../../models/operations/listcollaboratorsv2response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

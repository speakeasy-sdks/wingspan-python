# Collaborators
(*collaborators*)

### Available Operations

* [list](#list) - List all collaborators

## list

List all collaborators

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.collaborators.list()

if res.classes is not None:
    # handle response
    pass

```


### Response

**[operations.ListCollaboratorsResponse](../../models/operations/listcollaboratorsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

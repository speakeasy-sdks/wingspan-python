# CollaboratorsDetailsV2
(*collaborators_details_v2*)

### Available Operations

* [get](#get) - Get a list of collaborators and their details

## get

Get a list of collaborators and their details

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.collaborators_details_v2.get()

if res.classes is not None:
    # handle response
    pass

```


### Response

**[operations.GetCollaboratorsDetailsV2Response](../../models/operations/getcollaboratorsdetailsv2response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

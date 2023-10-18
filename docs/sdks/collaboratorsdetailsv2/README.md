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

if res.collaborators_report_responses is not None:
    # handle response
    pass
```


### Response

**[operations.GetCollaboratorsDetailsV2Response](../../models/operations/getcollaboratorsdetailsv2response.md)**


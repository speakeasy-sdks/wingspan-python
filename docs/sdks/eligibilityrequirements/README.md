# EligibilityRequirements
(*eligibility_requirements*)

### Available Operations

* [list](#list) - List Eligibility Requirements

## list

List Eligibility Requirements

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.eligibility_requirements.list()

if res.classes is not None:
    # handle response
    pass
```


### Response

**[operations.ListEligibilityRequirementsResponse](../../models/operations/listeligibilityrequirementsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

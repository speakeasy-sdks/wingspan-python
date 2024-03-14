# CollaboratorGroupEligibilityRequirement
(*collaborator_group_eligibility_requirement*)

### Available Operations

* [delete](#delete) - Delete Eligibility Requirement
* [replace](#replace) - Replace Eligibility Requirement

## delete

Delete Eligibility Requirement

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.collaborator_group_eligibility_requirement.delete(eligibility_requirement_id='<value>', id='<value>')

if res.collaborator_group_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                         | Type                              | Required                          | Description                       |
| --------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- |
| `eligibility_requirement_id`      | *str*                             | :heavy_check_mark:                | Unique eligibility Requirement Id |
| `id`                              | *str*                             | :heavy_check_mark:                | Unique identifier                 |


### Response

**[operations.DeleteCollaboratorGroupEligibilityRequirementResponse](../../models/operations/deletecollaboratorgroupeligibilityrequirementresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## replace

Replace Eligibility Requirement

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()


res = s.collaborator_group_eligibility_requirement.replace(eligibility_requirement_id='<value>', id='<value>', collaborator_group_requirement_update=shared.CollaboratorGroupRequirementUpdate(
    new_eligibility_requirement_id='<value>',
))

if res.collaborator_group_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `eligibility_requirement_id`                                                                                     | *str*                                                                                                            | :heavy_check_mark:                                                                                               | Unique eligibility Requirement Id                                                                                |
| `id`                                                                                                             | *str*                                                                                                            | :heavy_check_mark:                                                                                               | Unique identifier                                                                                                |
| `collaborator_group_requirement_update`                                                                          | [Optional[shared.CollaboratorGroupRequirementUpdate]](../../models/shared/collaboratorgrouprequirementupdate.md) | :heavy_minus_sign:                                                                                               | N/A                                                                                                              |


### Response

**[operations.ReplaceCollaboratorGroupEligibilityRequirementResponse](../../models/operations/replacecollaboratorgroupeligibilityrequirementresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

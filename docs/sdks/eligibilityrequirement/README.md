# EligibilityRequirement
(*eligibility_requirement*)

### Available Operations

* [create](#create) - Create Eligibility Requirement
* [delete](#delete) - Delete Eligibility Requirement
* [get](#get) - Get Eligibility Requirement
* [update](#update) - Update Eligibility Requirement

## create

Create Eligibility Requirement

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()

req = shared.EligibilityRequirementCreateRequest(
    requirement_type=shared.EligibilityRequirementCreateRequestRequirementType.SIGNATURE,
)

res = s.eligibility_requirement.create(req)

if res.eligibility_requirement is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [shared.EligibilityRequirementCreateRequest](../../models/shared/eligibilityrequirementcreaterequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.CreateEligibilityRequirementResponse](../../models/operations/createeligibilityrequirementresponse.md)**


## delete

Delete Eligibility Requirement

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.eligibility_requirement.delete(id='program')

if res.eligibility_requirements is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.DeleteEligibilityRequirementResponse](../../models/operations/deleteeligibilityrequirementresponse.md)**


## get

Get Eligibility Requirement

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.eligibility_requirement.get(id='female')

if res.eligibility_requirements is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.GetEligibilityRequirementResponse](../../models/operations/geteligibilityrequirementresponse.md)**


## update

Update Eligibility Requirement

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()


res = s.eligibility_requirement.update(id='Van', eligibility_requirement_update_request=shared.EligibilityRequirementUpdateRequest(
    requirement_type=shared.EligibilityRequirementUpdateRequestRequirementType.SIGNATURE,
))

if res.eligibility_requirements is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                               | *str*                                                                                                              | :heavy_check_mark:                                                                                                 | Unique identifier                                                                                                  |
| `eligibility_requirement_update_request`                                                                           | [Optional[shared.EligibilityRequirementUpdateRequest]](../../models/shared/eligibilityrequirementupdaterequest.md) | :heavy_minus_sign:                                                                                                 | N/A                                                                                                                |


### Response

**[operations.UpdateEligibilityRequirementResponse](../../models/operations/updateeligibilityrequirementresponse.md)**


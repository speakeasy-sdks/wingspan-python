# eligibility_requirement

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
    template_id='id',
    valid_for=6969.97,
)

res = s.eligibility_requirement.create(req)

if res.eligibility_requirement is not None:
    # handle response
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


res = s.eligibility_requirement.delete(id='neque')

if res.eligibility_requirements is not None:
    # handle response
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


res = s.eligibility_requirement.get(id='quo')

if res.eligibility_requirements is not None:
    # handle response
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


res = s.eligibility_requirement.update(id='illum', eligibility_requirement_update_request=shared.EligibilityRequirementUpdateRequest(
    requirement_type=shared.EligibilityRequirementUpdateRequestRequirementType.SIGNATURE,
    template_id='quo',
    valid_for=6813.59,
))

if res.eligibility_requirements is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                               | *str*                                                                                                              | :heavy_check_mark:                                                                                                 | Unique identifier                                                                                                  |
| `eligibility_requirement_update_request`                                                                           | [Optional[shared.EligibilityRequirementUpdateRequest]](../../models/shared/eligibilityrequirementupdaterequest.md) | :heavy_minus_sign:                                                                                                 | N/A                                                                                                                |


### Response

**[operations.UpdateEligibilityRequirementResponse](../../models/operations/updateeligibilityrequirementresponse.md)**


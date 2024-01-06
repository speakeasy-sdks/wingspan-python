# Collaborator
(*collaborator*)

### Available Operations

* [create](#create) - Create new collaborator
* [delete](#delete) - Delete collaborator by Id
* [get](#get) - Get collaborator by Id
* [update](#update) - Update a collaborator by Id

## create

Create new collaborator

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()

req = shared.CollaboratorCreateRequest(
    client_data=shared.ClientData(),
    client_id='string',
    form_w9_data=shared.MemberClientFormW9Info(
        address_line1='string',
        city='Jenafurt',
        company_structure=shared.CompanyStructureMemberClientFormW9Info.CORPORATION_C,
        country='Iraq',
        postal_code='17097',
        state='string',
    ),
    integration=shared.TwentySixe8ea23ccb1e007e7d6560175c7e75c768dac34727b7fe1d834ca24b8221ef4(
        quickbooks=shared.Sixa65bb5a9fe6d1135b7182baff68e9bc6612ee2c1ab942926fe2804c58663cf4(),
    ),
    labels={
        'key': 'string',
    },
)

res = s.collaborator.create(req)

if res.collaborator_schema is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [shared.CollaboratorCreateRequest](../../models/shared/collaboratorcreaterequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.CreateCollaboratorResponse](../../models/operations/createcollaboratorresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete

Delete collaborator by Id

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.collaborator.delete(id='string')

if res.collaborator_schema is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.DeleteCollaboratorResponse](../../models/operations/deletecollaboratorresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get

Get collaborator by Id

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.collaborator.get(id='string')

if res.collaborator_schema is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.GetCollaboratorResponse](../../models/operations/getcollaboratorresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update

Update a collaborator by Id

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()


res = s.collaborator.update(id='string', collaborator_update_request=shared.CollaboratorUpdateRequest(
    client_data=shared.ClientData(),
    form1099_balances=shared.Ninetyf96495b02c2509fff131505484d46479a91b7d23ed2b0f438ca117d0bccad7(
        two_thousand_and_twenty_one=shared.CollaboratorForm1099BalancesUpdateRequest(
            correction=shared.Ce853dbef33b2b91880690c84bc5314340c1301fd7b3503dd6ce79c844e2a481(
                address=shared.Ce853dbef33b2b91880690c84bc5314340c1301fd7b3503dd6ce79c844e2a481Address(),
            ),
            dispute=shared.Eighta9c6cb49482a98cdd603ff09858cdc3e5ef6ad9807c876c4161d925a96694a5(),
            events=shared.Events(),
        ),
        two_thousand_and_twenty_two=shared.CollaboratorForm1099BalancesUpdateRequest(
            correction=shared.Ce853dbef33b2b91880690c84bc5314340c1301fd7b3503dd6ce79c844e2a481(
                address=shared.Ce853dbef33b2b91880690c84bc5314340c1301fd7b3503dd6ce79c844e2a481Address(),
            ),
            dispute=shared.Eighta9c6cb49482a98cdd603ff09858cdc3e5ef6ad9807c876c4161d925a96694a5(),
            events=shared.Events(),
        ),
    ),
    form_w9_data=shared.FormW9Data(),
    integration=shared.TwentySixe8ea23ccb1e007e7d6560175c7e75c768dac34727b7fe1d834ca24b8221ef4(
        quickbooks=shared.Sixa65bb5a9fe6d1135b7182baff68e9bc6612ee2c1ab942926fe2804c58663cf4(),
    ),
    labels={
        'key': 'string',
    },
))

if res.collaborator_schema is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `id`                                                                                           | *str*                                                                                          | :heavy_check_mark:                                                                             | Unique identifier                                                                              |
| `collaborator_update_request`                                                                  | [Optional[shared.CollaboratorUpdateRequest]](../../models/shared/collaboratorupdaterequest.md) | :heavy_minus_sign:                                                                             | N/A                                                                                            |


### Response

**[operations.UpdateCollaboratorResponse](../../models/operations/updatecollaboratorresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

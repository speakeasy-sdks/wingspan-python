# Collaborator

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
    client_data=shared.ClientData(
        auto_pay_strategy=shared.AutoPayStrategyClientData.ALL,
        external_id='soluta',
        verification_stratgy=shared.VerificationStratgyClientData.LESS_THAN_NIL_GREATER_THAN_,
    ),
    client_id='iusto',
    collaborator_group_id='voluptate',
    form_w9_data=shared.MemberClientFormW9Info(
        address_line1='deleniti',
        address_line2='omnis',
        city='Portland',
        company_structure=shared.CompanyStructureMemberClientFormW9Info.PARTNERSHIP,
        country='Republic of Korea',
        dob='ipsum',
        ein='voluptate',
        first_name='Makenzie',
        last_name='Ullrich',
        legal_business_name='eius',
        postal_code='02783',
        ssn='saepe',
        state='suscipit',
    ),
    integration=shared.TwentySixe8ea23ccb1e007e7d6560175c7e75c768dac34727b7fe1d834ca24b8221ef4(
        quickbooks=shared.Sixa65bb5a9fe6d1135b7182baff68e9bc6612ee2c1ab942926fe2804c58663cf4(
            expense_account_id='minima',
            vendor_id='repellendus',
        ),
    ),
    labels={
        "similique": 'alias',
    },
    member_company='at',
    member_email='quaerat',
    member_id='tempora',
    member_name='vel',
    status=shared.StatusCollaboratorCreateRequest.LESS_THAN_NIL_GREATER_THAN_,
)

res = s.collaborator.create(req)

if res.collaborator_schema is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [shared.CollaboratorCreateRequest](../../models/shared/collaboratorcreaterequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.CreateCollaboratorResponse](../../models/operations/createcollaboratorresponse.md)**


## delete

Delete collaborator by Id

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.collaborator.delete(id='officiis')

if res.collaborator_schema is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.DeleteCollaboratorResponse](../../models/operations/deletecollaboratorresponse.md)**


## get

Get collaborator by Id

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.collaborator.get(id='qui')

if res.collaborator_schema is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.GetCollaboratorResponse](../../models/operations/getcollaboratorresponse.md)**


## update

Update a collaborator by Id

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()


res = s.collaborator.update(id='dolorum', collaborator_update_request=shared.CollaboratorUpdateRequest(
    client_data=shared.ClientData(
        auto_pay_strategy=shared.AutoPayStrategyClientData.NONE,
        external_id='harum',
        verification_stratgy=shared.VerificationStratgyClientData.ALL,
    ),
    form1099_balances='quisquam',
    form_w9_data=shared.CollaboratorUpdateRequestFormW9Data2(),
    integration='tempore',
    labels={
        "numquam": 'enim',
    },
    status=shared.StatusCollaboratorUpdateRequest.ACTIVE,
))

if res.collaborator_schema is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `id`                                                                                           | *str*                                                                                          | :heavy_check_mark:                                                                             | Unique identifier                                                                              |
| `collaborator_update_request`                                                                  | [Optional[shared.CollaboratorUpdateRequest]](../../models/shared/collaboratorupdaterequest.md) | :heavy_minus_sign:                                                                             | N/A                                                                                            |


### Response

**[operations.UpdateCollaboratorResponse](../../models/operations/updatecollaboratorresponse.md)**


# collaborator

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
        auto_pay_strategy=shared.AutoPayStrategyClientData.LESS_THAN_NIL_GREATER_THAN_,
        external_id='doloribus',
        verification_stratgy=shared.VerificationStratgyClientData.NONE,
    ),
    client_id='facilis',
    collaborator_group_id='cupiditate',
    form_w9_data='quae',
    integration=shared.TwentySixe8ea23ccb1e007e7d6560175c7e75c768dac34727b7fe1d834ca24b8221ef4(
        quickbooks='occaecati',
    ),
    labels={
        "vero": 'omnis',
        "quis": 'ipsum',
        "delectus": 'voluptate',
        "consectetur": 'vero',
    },
    member_company='tenetur',
    member_email='dignissimos',
    member_id='hic',
    member_name='distinctio',
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


res = s.collaborator.delete(id='odio')

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


res = s.collaborator.get(id='similique')

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


res = s.collaborator.update(id='facilis', collaborator_update_request=shared.CollaboratorUpdateRequest(
    client_data=shared.ClientData(
        auto_pay_strategy=shared.AutoPayStrategyClientData.NONE,
        external_id='dolore',
        verification_stratgy=shared.VerificationStratgyClientData.LESS_THAN_NIL_GREATER_THAN_,
    ),
    form1099_balances=shared.Ninetyf96495b02c2509fff131505484d46479a91b7d23ed2b0f438ca117d0bccad7(
        two_thousand_and_twenty_one='natus',
        two_thousand_and_twenty_two=shared.CollaboratorForm1099BalancesUpdateRequest(
            adjustments=132.36,
            correction=shared.Ce853dbef33b2b91880690c84bc5314340c1301fd7b3503dd6ce79c844e2a481(
                address='nulla',
                company_structure=shared.CompanyStructurece853dbef33b2b91880690c84bc5314340c1301fd7b3503dd6ce79c844e2a481.SOLE_PROPRIETORSHIP,
                ein='porro',
                first_name='Willie',
                last_name='Wyman',
                legal_business_name='iusto',
                ssn='eligendi',
                total_amount=4973.91,
            ),
            delivery_method=shared.DeliveryMethodCollaboratorForm1099BalancesUpdateRequest.ELECTRONIC,
            dispute=shared.Eighta9c6cb49482a98cdd603ff09858cdc3e5ef6ad9807c876c4161d925a96694a5(
                amount=2694.79,
                comment='ipsam',
                status=shared.Status8a9c6cb49482a98cdd603ff09858cdc3e5ef6ad9807c876c4161d925a96694a5.ACCEPTED,
            ),
            events='vel',
            status=shared.StatusCollaboratorForm1099BalancesUpdateRequest.EXCLUDED,
        ),
    ),
    form_w9_data='ratione',
    integration='laudantium',
    labels='dolor',
    status=shared.StatusCollaboratorUpdateRequest.LESS_THAN_NIL_GREATER_THAN_,
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


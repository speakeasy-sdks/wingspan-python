# member_client

### Available Operations

* [create](#create) - Create memberClient
* [delete](#delete) - Delete memberClient
* [get](#get) - Get Member Client
* [update](#update) - Update memberClient

## create

Create memberClient

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()

req = shared.MemberClientCreateRequest(
    client_id='impedit',
    company='Hirthe Inc',
    email_cc=[
        'dicta',
        'maiores',
    ],
    email_to='natus',
    integration='voluptatibus',
    labels='asperiores',
    member_data='ea',
    member_id='quaerat',
    name='Kari Nikolaus',
    status=shared.StatusMemberClientCreateRequest.PENDING,
)

res = s.member_client.create(req)

if res.member_client_schema is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [shared.MemberClientCreateRequest](../../models/shared/memberclientcreaterequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.CreateMemberClientResponse](../../models/operations/creatememberclientresponse.md)**


## delete

Delete memberClient

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.member_client.delete(id='asperiores')

if res.member_client_schema is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.DeleteMemberClientResponse](../../models/operations/deletememberclientresponse.md)**


## get

Get Member Client

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.member_client.get(id='nemo')

if res.member_client_schema is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.GetMemberClientResponse](../../models/operations/getmemberclientresponse.md)**


## update

Update memberClient

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()


res = s.member_client.update(id='quae', member_client_update_request=shared.MemberClientUpdateRequest(
    client_data='porro',
    client_id='quod',
    company='Bernier Inc',
    email_cc=[
        'id',
        'suscipit',
        'velit',
    ],
    email_to='culpa',
    form1099_balances=shared.Ninetyf96495b02c2509fff131505484d46479a91b7d23ed2b0f438ca117d0bccad7(
        two_thousand_and_twenty_one=shared.CollaboratorForm1099BalancesUpdateRequest(
            adjustments=5173.09,
            correction=shared.Ce853dbef33b2b91880690c84bc5314340c1301fd7b3503dd6ce79c844e2a481(
                address='ducimus',
                company_structure=shared.CompanyStructurece853dbef33b2b91880690c84bc5314340c1301fd7b3503dd6ce79c844e2a481.LLC_CORPORATION_C,
                ein='vel',
                first_name='Edmund',
                last_name='Senger',
                legal_business_name='facilis',
                ssn='cum',
                total_amount=4148.57,
            ),
            delivery_method=shared.DeliveryMethodCollaboratorForm1099BalancesUpdateRequest.MAIL,
            dispute='reiciendis',
            events=shared.CollaboratorForm1099BalancesUpdateRequestEvents2(),
            status=shared.StatusCollaboratorForm1099BalancesUpdateRequest.NEEDS_ACTION_DISPUTE,
        ),
        two_thousand_and_twenty_two=shared.CollaboratorForm1099BalancesUpdateRequest(
            adjustments=3975.33,
            correction='cum',
            delivery_method=shared.DeliveryMethodCollaboratorForm1099BalancesUpdateRequest.ELECTRONIC,
            dispute='exercitationem',
            events=shared.CollaboratorForm1099BalancesUpdateRequestEvents2(),
            status=shared.StatusCollaboratorForm1099BalancesUpdateRequest.EXCLUDED,
        ),
    ),
    form_w9_data='doloribus',
    integration='reiciendis',
    labels={
        "necessitatibus": 'dolore',
        "sunt": 'asperiores',
        "adipisci": 'non',
        "amet": 'beatae',
    },
    member_data='a',
    name='Glenn Herzog',
    status=shared.StatusMemberClientUpdateRequest.ACTIVE,
))

if res.member_client_schema is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `id`                                                                                           | *str*                                                                                          | :heavy_check_mark:                                                                             | Unique identifier                                                                              |
| `member_client_update_request`                                                                 | [Optional[shared.MemberClientUpdateRequest]](../../models/shared/memberclientupdaterequest.md) | :heavy_minus_sign:                                                                             | N/A                                                                                            |


### Response

**[operations.UpdateMemberClientResponse](../../models/operations/updatememberclientresponse.md)**


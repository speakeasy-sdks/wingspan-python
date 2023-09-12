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
    client_id='consequatur',
    company='Toy and Sons',
    email_cc=[
        'aspernatur',
    ],
    email_to='sequi',
    integration=shared.D750b2d9403b5bcbdb3c96c89f1cc713df563d587f16e5f39f5ab546c08a20a0(
        quickbooks='recusandae',
    ),
    labels='distinctio',
    member_data=shared.MemberData(
        auto_pay_requirement=shared.AutoPayRequirementMemberData.NONE,
        external_id='inventore',
        share_tax_document=shared.ShareTaxDocumentMemberData.DECLINE,
    ),
    member_id='totam',
    name='Tom Kuhn',
    status=shared.StatusMemberClientCreateRequest.LESS_THAN_NIL_GREATER_THAN_,
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


res = s.member_client.delete(id='dolores')

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


res = s.member_client.get(id='deserunt')

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


res = s.member_client.update(id='molestiae', member_client_update_request=shared.MemberClientUpdateRequest(
    client_data='porro',
    client_id='eum',
    company='Langosh - Cronin',
    email_cc=[
        'deleniti',
    ],
    email_to='fugit',
    form1099_balances=shared.Ninetyf96495b02c2509fff131505484d46479a91b7d23ed2b0f438ca117d0bccad7(
        two_thousand_and_twenty_one=shared.CollaboratorForm1099BalancesUpdateRequest(
            adjustments=2775.96,
            correction=shared.Ce853dbef33b2b91880690c84bc5314340c1301fd7b3503dd6ce79c844e2a481(
                address='minima',
                company_structure=shared.CompanyStructurece853dbef33b2b91880690c84bc5314340c1301fd7b3503dd6ce79c844e2a481.CORPORATION_S,
                ein='fugit',
                first_name='Verlie',
                last_name='Cronin',
                legal_business_name='ratione',
                ssn='explicabo',
                total_amount=9039.84,
            ),
            delivery_method=shared.DeliveryMethodCollaboratorForm1099BalancesUpdateRequest.BOTH,
            dispute=shared.Eighta9c6cb49482a98cdd603ff09858cdc3e5ef6ad9807c876c4161d925a96694a5(
                amount=922.6,
                comment='esse',
                status=shared.Status8a9c6cb49482a98cdd603ff09858cdc3e5ef6ad9807c876c4161d925a96694a5.LESS_THAN_NIL_GREATER_THAN_,
            ),
            events=shared.CollaboratorForm1099BalancesUpdateRequestEvents2(),
            status=shared.StatusCollaboratorForm1099BalancesUpdateRequest.READY,
        ),
        two_thousand_and_twenty_two='quod',
    ),
    form_w9_data=shared.MemberClientUpdateRequestFormW9Data2(),
    integration=shared.Threed33fba3f009de957b3be92fba006d6383af7e39f823cc1fd213506f6205100f(
        quickbooks='quasi',
    ),
    labels={
        "vel": 'harum',
    },
    member_data='rerum',
    name='Warren Rau V',
    status=shared.StatusMemberClientUpdateRequest.PENDING,
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


# MemberClient
(*member_client*)

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
    email_cc=[
        'string',
    ],
    integration=shared.D750b2d9403b5bcbdb3c96c89f1cc713df563d587f16e5f39f5ab546c08a20a0(
        quickbooks=shared.SixtyFourMillionEightHundredAndFortySixThousandOneHundredAndThirtySixa354aa510825c1f23c3a978f4c816d8d4184311e7294a570f73727dc(),
    ),
    labels={
        'key': 'string',
    },
    member_data=shared.MemberData(),
)

res = s.member_client.create(req)

if res.member_client_schema is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [shared.MemberClientCreateRequest](../../models/shared/memberclientcreaterequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.CreateMemberClientResponse](../../models/operations/creatememberclientresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## delete

Delete memberClient

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.member_client.delete(id='string')

if res.member_client_schema is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.DeleteMemberClientResponse](../../models/operations/deletememberclientresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get

Get Member Client

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.member_client.get(id='string')

if res.member_client_schema is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.GetMemberClientResponse](../../models/operations/getmemberclientresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## update

Update memberClient

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()


res = s.member_client.update(id='string', member_client_update_request=shared.MemberClientUpdateRequest(
    client_data=shared.ClientData(),
    email_cc=[
        'string',
    ],
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
    form_w9_data=shared.MemberClientUpdateRequestFormW9Data(),
    integration=shared.Threed33fba3f009de957b3be92fba006d6383af7e39f823cc1fd213506f6205100f(
        quickbooks=shared.D86c1fba5267ac3d9ce2954a6e46b70e471c0f91a44abbe94565ae50e6e9e863(),
    ),
    labels={
        'key': 'string',
    },
    member_data=shared.MemberData(),
))

if res.member_client_schema is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `id`                                                                                           | *str*                                                                                          | :heavy_check_mark:                                                                             | Unique identifier                                                                              |
| `member_client_update_request`                                                                 | [Optional[shared.MemberClientUpdateRequest]](../../models/shared/memberclientupdaterequest.md) | :heavy_minus_sign:                                                                             | N/A                                                                                            |


### Response

**[operations.UpdateMemberClientResponse](../../models/operations/updatememberclientresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

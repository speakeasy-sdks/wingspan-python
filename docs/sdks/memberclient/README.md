# MemberClient

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
    client_id='tempora',
    company='Cole LLC',
    email_cc=[
        'ipsa',
    ],
    email_to='molestiae',
    integration='odio',
    labels='esse',
    member_data='rem',
    member_id='fuga',
    name='Yvette Stehr',
    status=shared.StatusMemberClientCreateRequest.INACTIVE,
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


res = s.member_client.delete(id='assumenda')

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


res = s.member_client.get(id='eos')

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


res = s.member_client.update(id='praesentium', member_client_update_request=shared.MemberClientUpdateRequest(
    client_data=shared.ClientData(
        auto_pay_strategy=shared.AutoPayStrategyClientData.ALL,
        external_id='ipsa',
        verification_stratgy=shared.VerificationStratgyClientData.ALL,
    ),
    client_id='quidem',
    company='Satterfield Group',
    email_cc=[
        'quo',
    ],
    email_to='fuga',
    form1099_balances='eos',
    form_w9_data='ab',
    integration=shared.Threed33fba3f009de957b3be92fba006d6383af7e39f823cc1fd213506f6205100f(
        quickbooks='tempora',
    ),
    labels={
        "ipsam": 'aspernatur',
    },
    member_data='quo',
    name='Sophie Bayer',
    status=shared.StatusMemberClientUpdateRequest.INACTIVE,
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


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
    client_id='ipsa',
    company='Kuhlman - Hahn',
    email_cc=[
        'accusamus',
    ],
    email_to='quidem',
    integration=[],
    labels=[],
    member_data=[],
    member_id='voluptatibus',
    name='Faye Daugherty PhD',
    status=shared.StatusMemberClientCreateRequest.ACTIVE,
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


res = s.member_client.delete(id='soluta')

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


res = s.member_client.get(id='dolorum')

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


res = s.member_client.update(id='iusto', member_client_update_request=shared.MemberClientUpdateRequest(
    client_data=[],
    client_id='voluptate',
    company='Leuschke, Mohr and Treutel',
    email_cc=[
        'distinctio',
    ],
    email_to='asperiores',
    form1099_balances=[],
    form_w9_data=[],
    integration=[],
    labels=[],
    member_data=[],
    name='Edna Klocko',
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


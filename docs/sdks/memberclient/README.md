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

req = shared.MemberClientCreateRequest()

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
| errors.SDKError | 4x-5xx          | */*             |

## delete

Delete memberClient

### Example Usage

```python
import wingspan

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
| errors.SDKError | 4x-5xx          | */*             |

## get

Get Member Client

### Example Usage

```python
import wingspan

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
| errors.SDKError | 4x-5xx          | */*             |

## update

Update memberClient

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()


res = s.member_client.update(id='string', member_client_update_request=shared.MemberClientUpdateRequest())

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
| errors.SDKError | 4x-5xx          | */*             |

# AdditionalData
(*additional_data*)

### Available Operations

* [create](#create) - Create additional data
* [delete](#delete) - Delete additional data
* [get](#get) - Get additional data

## create

Create additional data

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()

req = shared.AdditionalData(
    key='<key>',
    name='online',
    required=False,
    type=shared.AdditionalDataType.STRING,
)

res = s.additional_data.create(req)

if res.additional_data is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `request`                                                      | [shared.AdditionalData](../../models/shared/additionaldata.md) | :heavy_check_mark:                                             | The request object to use for the request.                     |


### Response

**[operations.CreateAdditionalDataResponse](../../models/operations/createadditionaldataresponse.md)**


## delete

Delete additional data

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.additional_data.delete(id='program')

if res.additional_data is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.DeleteAdditionalDataResponse](../../models/operations/deleteadditionaldataresponse.md)**


## get

Get additional data

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.additional_data.get(id='female')

if res.additional_data is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.GetAdditionalDataResponse](../../models/operations/getadditionaldataresponse.md)**


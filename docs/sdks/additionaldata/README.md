# additional_data

### Available Operations

* [create](#create) - Create additional data
* [delete](#delete) - Delete additional data
* [get](#get) - Get additional data

## create

Create additional data

### Example Usage

```python
import petstore
from petstore.models import shared

s = petstore.Petstore()

req = shared.AdditionalData(
    key='corrupti',
    name='Ben Mueller',
    required=False,
    type=shared.AdditionalDataType.BOOLEAN,
)

res = s.additional_data.create(req)

if res.additional_data is not None:
    # handle response
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
import petstore
from petstore.models import operations

s = petstore.Petstore()

req = operations.DeleteAdditionalDataRequest(
    id='4e0f467c-c879-46ed-951a-05dfc2ddf7cc',
)

res = s.additional_data.delete(req)

if res.additional_data is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.DeleteAdditionalDataRequest](../../models/operations/deleteadditionaldatarequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.DeleteAdditionalDataResponse](../../models/operations/deleteadditionaldataresponse.md)**


## get

Get additional data

### Example Usage

```python
import petstore
from petstore.models import operations

s = petstore.Petstore()

req = operations.GetAdditionalDataRequest(
    id='78ca1ba9-28fc-4816-b42c-b73920592939',
)

res = s.additional_data.get(req)

if res.additional_data is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetAdditionalDataRequest](../../models/operations/getadditionaldatarequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.GetAdditionalDataResponse](../../models/operations/getadditionaldataresponse.md)**


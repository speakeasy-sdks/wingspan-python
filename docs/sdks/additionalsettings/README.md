# AdditionalSettings
(*additional_settings*)

### Available Operations

* [list](#list) - List additional settings
* [update](#update) - Update additional settings

## list

List additional settings

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.additional_settings.list()

if res.classes is not None:
    # handle response
    pass
```


### Response

**[operations.ListAdditionalSettingsResponse](../../models/operations/listadditionalsettingsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update

Update additional settings

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()


res = s.additional_settings.update(id='string', additional_data_update_request=shared.AdditionalDataUpdateRequest())

if res.additional_data is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `id`                                                                                               | *str*                                                                                              | :heavy_check_mark:                                                                                 | Unique identifier                                                                                  |
| `additional_data_update_request`                                                                   | [Optional[shared.AdditionalDataUpdateRequest]](../../models/shared/additionaldataupdaterequest.md) | :heavy_minus_sign:                                                                                 | N/A                                                                                                |


### Response

**[operations.UpdateAdditionalSettingsResponse](../../models/operations/updateadditionalsettingsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

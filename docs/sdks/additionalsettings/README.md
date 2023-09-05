# additional_settings

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

if res.additional_data is not None:
    # handle response
```


### Response

**[operations.ListAdditionalSettingsResponse](../../models/operations/listadditionalsettingsresponse.md)**


## update

Update additional settings

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()


res = s.additional_settings.update(id='deserunt', additional_data_update_request=shared.AdditionalDataUpdateRequest(
    key='perferendis',
    name='Estelle Will',
    required=False,
    type=shared.TypeAdditionalDataUpdateRequest.LESS_THAN_NIL_GREATER_THAN_,
))

if res.additional_data is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `id`                                                                                               | *str*                                                                                              | :heavy_check_mark:                                                                                 | Unique identifier                                                                                  |
| `additional_data_update_request`                                                                   | [Optional[shared.AdditionalDataUpdateRequest]](../../models/shared/additionaldataupdaterequest.md) | :heavy_minus_sign:                                                                                 | N/A                                                                                                |


### Response

**[operations.UpdateAdditionalSettingsResponse](../../models/operations/updateadditionalsettingsresponse.md)**


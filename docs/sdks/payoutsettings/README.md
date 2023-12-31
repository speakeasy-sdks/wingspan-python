# PayoutSettings
(*payout_settings*)

### Available Operations

* [get](#get) - Get the payout settings
* [update](#update) - Update the payout settings

## get

Get the payout settings

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.payout_settings.get(id='female')

if res.payout_settings_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.GetPayoutSettingsResponse](../../models/operations/getpayoutsettingsresponse.md)**


## update

Update the payout settings

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()


res = s.payout_settings.update(id='Van', payout_settings_update=shared.PayoutSettingsUpdate(
    payout_destinations=[
        shared.PayoutDestinationUpdate(),
    ],
))

if res.payout_settings_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `id`                                                                                 | *str*                                                                                | :heavy_check_mark:                                                                   | Unique identifier                                                                    |
| `payout_settings_update`                                                             | [Optional[shared.PayoutSettingsUpdate]](../../models/shared/payoutsettingsupdate.md) | :heavy_minus_sign:                                                                   | N/A                                                                                  |


### Response

**[operations.UpdatePayoutSettingsResponse](../../models/operations/updatepayoutsettingsresponse.md)**


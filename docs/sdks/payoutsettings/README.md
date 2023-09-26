# PayoutSettings

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


res = s.payout_settings.get(id='minima')

if res.payout_settings_response is not None:
    # handle response
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


res = s.payout_settings.update(id='nobis', payout_settings_update=shared.PayoutSettingsUpdate(
    payout_destinations=[
        shared.PayoutDestinationUpdate(
            destination_id='adipisci',
            destination_type=shared.DestinationTypePayoutDestinationUpdate.LESS_THAN_NIL_GREATER_THAN_,
            payout_method=shared.PayoutMethodPayoutDestinationUpdate.INSTANT,
            percentage=5039.34,
        ),
    ],
    payout_preferences=shared.PayoutPreferencesPayoutSettingsUpdate.EXPEDITED,
))

if res.payout_settings_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `id`                                                                                 | *str*                                                                                | :heavy_check_mark:                                                                   | Unique identifier                                                                    |
| `payout_settings_update`                                                             | [Optional[shared.PayoutSettingsUpdate]](../../models/shared/payoutsettingsupdate.md) | :heavy_minus_sign:                                                                   | N/A                                                                                  |


### Response

**[operations.UpdatePayoutSettingsResponse](../../models/operations/updatepayoutsettingsresponse.md)**


# payout_settings

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


res = s.payout_settings.get(id='provident')

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


res = s.payout_settings.update(id='earum', payout_settings_update=shared.PayoutSettingsUpdate(
    payout_destinations=[
        shared.PayoutDestinationUpdate(
            destination_id='illum',
            destination_type=shared.DestinationTypePayoutDestinationUpdate.ACCOUNT,
            payout_method=shared.PayoutMethodPayoutDestinationUpdate.LESS_THAN_NIL_GREATER_THAN_,
            percentage=5962.11,
        ),
        shared.PayoutDestinationUpdate(
            destination_id='debitis',
            destination_type=shared.DestinationTypePayoutDestinationUpdate.CARD,
            payout_method=shared.PayoutMethodPayoutDestinationUpdate.E_CHECK,
            percentage=3803.35,
        ),
        'fugit',
    ],
    payout_preferences=shared.PayoutPreferencesPayoutSettingsUpdate.E_CHECK,
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


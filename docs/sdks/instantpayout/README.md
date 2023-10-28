# InstantPayout
(*instant_payout*)

### Available Operations

* [create](#create) - Create instant payout details
* [delete](#delete) - Delete instant payout
* [fetch](#fetch) - Fetch instant payout details

## create

Create instant payout details

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()

req = shared.InstantPayoutRequest(
    external_payout_account_token='string',
)

res = s.instant_payout.create(req)

if res.instant_payout_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [shared.InstantPayoutRequest](../../models/shared/instantpayoutrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.CreateInstantPayoutResponse](../../models/operations/createinstantpayoutresponse.md)**


## delete

Delete instant payout

### Example Usage

```python
import wingspan


s = wingspan.Wingspan()


res = s.instant_payout.delete()

if res.instant_payout_response is not None:
    # handle response
    pass
```


### Response

**[operations.DeleteInstantPayoutResponse](../../models/operations/deleteinstantpayoutresponse.md)**


## fetch

Fetch instant payout details

### Example Usage

```python
import wingspan


s = wingspan.Wingspan()


res = s.instant_payout.fetch()

if res.instant_payout_response is not None:
    # handle response
    pass
```


### Response

**[operations.FetchInstantPayoutResponse](../../models/operations/fetchinstantpayoutresponse.md)**


# PayoutDebitCards
(*payout_debit_cards*)

### Available Operations

* [list](#list) - List the payout debit cards

## list

List the payout debit cards

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.payout_debit_cards.list(member_id='string')

if res.classes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                     | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `member_id`                   | *str*                         | :heavy_check_mark:            | Unique identifier of a member |


### Response

**[operations.ListPayoutDebitCardsResponse](../../models/operations/listpayoutdebitcardsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

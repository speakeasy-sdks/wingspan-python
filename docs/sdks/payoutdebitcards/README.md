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


res = s.payout_debit_cards.list(member_id='Bicycle')

if res.checkbook_cards is not None:
    # handle response
```

### Parameters

| Parameter                     | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `member_id`                   | *str*                         | :heavy_check_mark:            | Unique identifier of a member |


### Response

**[operations.ListPayoutDebitCardsResponse](../../models/operations/listpayoutdebitcardsresponse.md)**


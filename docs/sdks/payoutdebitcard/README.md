# PayoutDebitCard
(*payout_debit_card*)

### Available Operations

* [create](#create) - Create a payout debit card
* [delete](#delete) - Delete the payout debit card
* [get](#get) - Get the payout debit card

## create

Create a payout debit card

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()


res = s.payout_debit_card.create(member_id='online', checkbook_card_create=shared.CheckbookCardCreate(
    address=shared.Address(
        address_line1='Configuration',
        city='Edwardoville',
        postal_code='09739-8041',
        state='evolve',
    ),
    card_number='male',
    exp_mm='SUV',
    exp_yyyy='quantify',
    name='Polestar',
))

if res.checkbook_card is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `member_id`                                                                        | *str*                                                                              | :heavy_check_mark:                                                                 | Unique identifier of a member                                                      |
| `checkbook_card_create`                                                            | [Optional[shared.CheckbookCardCreate]](../../models/shared/checkbookcardcreate.md) | :heavy_minus_sign:                                                                 | N/A                                                                                |


### Response

**[operations.CreatePayoutDebitCardResponse](../../models/operations/createpayoutdebitcardresponse.md)**


## delete

Delete the payout debit card

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.payout_debit_card.delete(id='program', member_id='Designer')

if res.checkbook_card is not None:
    # handle response
    pass
```

### Parameters

| Parameter                     | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `id`                          | *str*                         | :heavy_check_mark:            | Unique identifier             |
| `member_id`                   | *str*                         | :heavy_check_mark:            | Unique identifier of a member |


### Response

**[operations.DeletePayoutDebitCardResponse](../../models/operations/deletepayoutdebitcardresponse.md)**


## get

Get the payout debit card

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.payout_debit_card.get(id='female', member_id='program')

if res.checkbook_card is not None:
    # handle response
    pass
```

### Parameters

| Parameter                     | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `id`                          | *str*                         | :heavy_check_mark:            | Unique identifier             |
| `member_id`                   | *str*                         | :heavy_check_mark:            | Unique identifier of a member |


### Response

**[operations.GetPayoutDebitCardResponse](../../models/operations/getpayoutdebitcardresponse.md)**


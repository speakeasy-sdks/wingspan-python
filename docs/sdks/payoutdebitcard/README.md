# PayoutDebitCard

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


res = s.payout_debit_card.create(member_id='saepe', checkbook_card_create=shared.CheckbookCardCreate(
    address=shared.Address(
        address_line1='dolore',
        address_line2='sunt',
        city='Deltona',
        postal_code='21498',
        state='consectetur',
    ),
    card_number='corporis',
    cvv='harum',
    exp_mm='laboriosam',
    exp_yyyy='ipsa',
    name='Randolph Bruen',
))

if res.checkbook_card is not None:
    # handle response
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


res = s.payout_debit_card.delete(id='tempora', member_id='aspernatur')

if res.checkbook_card is not None:
    # handle response
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


res = s.payout_debit_card.get(id='voluptas', member_id='voluptas')

if res.checkbook_card is not None:
    # handle response
```

### Parameters

| Parameter                     | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `id`                          | *str*                         | :heavy_check_mark:            | Unique identifier             |
| `member_id`                   | *str*                         | :heavy_check_mark:            | Unique identifier of a member |


### Response

**[operations.GetPayoutDebitCardResponse](../../models/operations/getpayoutdebitcardresponse.md)**


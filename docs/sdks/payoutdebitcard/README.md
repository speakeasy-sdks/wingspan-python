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


res = s.payout_debit_card.create(member_id='string', checkbook_card_create=shared.CheckbookCardCreate(
    address=shared.Address(
        address_line1='string',
        city='Jenafurt',
        postal_code='42170-9739',
        state='string',
    ),
    card_number='string',
    exp_mm='string',
    exp_yyyy='string',
    name='string',
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## delete

Delete the payout debit card

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.payout_debit_card.delete(id='string', member_id='string')

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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get

Get the payout debit card

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.payout_debit_card.get(id='string', member_id='string')

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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

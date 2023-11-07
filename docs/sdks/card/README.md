# Card
(*.card*)

### Available Operations

* [create](#create) - Create card
* [delete](#delete) - Delete a card by cardId
* [get](#get) - Get card by cardId
* [update](#update) - Update card by cardId

## create

Create card

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()

req = shared.CardCreateRequest(
    shipping_address=shared.Address(
        address_line1='string',
        city='Jenafurt',
        postal_code='42170-9739',
        state='string',
    ),
)

res = s.card.create(req)

if res.card is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [shared.CardCreateRequest](../../models/shared/cardcreaterequest.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.CreateCardResponse](../../models/operations/createcardresponse.md)**


## delete

Delete a card by cardId

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.card.delete(id='string')

if res.card is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.DeleteCardResponse](../../models/operations/deletecardresponse.md)**


## get

Get card by cardId

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.card.get(id='string')

if res.card_details is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.GetCardResponse](../../models/operations/getcardresponse.md)**


## update

Update card by cardId

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()


res = s.card.update(id='string', card_update_request=shared.CardUpdateRequest(
    status=shared.PropertiesCardUpdateRequest.CLOSED_BY_CUSTOMER,
))

if res.card is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `id`                                                                           | *str*                                                                          | :heavy_check_mark:                                                             | Unique identifier                                                              |
| `card_update_request`                                                          | [Optional[shared.CardUpdateRequest]](../../models/shared/cardupdaterequest.md) | :heavy_minus_sign:                                                             | N/A                                                                            |


### Response

**[operations.UpdateCardResponse](../../models/operations/updatecardresponse.md)**


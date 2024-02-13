# Card
(*card*)

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

req = shared.CardCreateRequest()

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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete

Delete a card by cardId

### Example Usage

```python
import wingspan

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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get

Get card by cardId

### Example Usage

```python
import wingspan

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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update

Update card by cardId

### Example Usage

```python
import wingspan
from wingspan.models import shared

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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

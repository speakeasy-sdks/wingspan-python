# card

### Available Operations

* [delete](#delete) - Delete a card by cardId
* [update](#update) - Update card by cardId

## delete

Delete a card by cardId

### Example Usage

```python
import petstore
from petstore.models import operations

s = petstore.Petstore()

req = operations.DeleteCardRequest(
    id='ea7596eb-10fa-4aa2-b52c-5955907aff1a',
)

res = s.card.delete(req)

if res.card is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.DeleteCardRequest](../../models/operations/deletecardrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.DeleteCardResponse](../../models/operations/deletecardresponse.md)**


## update

Update card by cardId

### Example Usage

```python
import petstore
from petstore.models import operations, shared

s = petstore.Petstore()

req = operations.UpdateCardRequest(
    card_update_request=shared.CardUpdateRequest(
        status=shared.CardUpdateRequestStatus.INACTIVE,
    ),
    id='a2fa9467-7392-451a-a52c-3f5ad019da1f',
)

res = s.card.update(req)

if res.card is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.UpdateCardRequest](../../models/operations/updatecardrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.UpdateCardResponse](../../models/operations/updatecardresponse.md)**


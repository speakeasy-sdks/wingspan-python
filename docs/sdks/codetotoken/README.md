# CodeToToken
(*code_to_token*)

### Available Operations

* [exchange](#exchange) - Exchange the code for a token

## exchange

Exchange the code for a token

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()


res = s.code_to_token.exchange(id='dolor', card_token_request=shared.CardTokenRequest(
    verification_code='necessitatibus',
    verification_token='odit',
))

if res.card_token_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `id`                                                                         | *str*                                                                        | :heavy_check_mark:                                                           | Unique identifier                                                            |
| `card_token_request`                                                         | [Optional[shared.CardTokenRequest]](../../models/shared/cardtokenrequest.md) | :heavy_minus_sign:                                                           | N/A                                                                          |


### Response

**[operations.ExchangeCodeToTokenResponse](../../models/operations/exchangecodetotokenresponse.md)**


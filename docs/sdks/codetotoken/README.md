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


res = s.code_to_token.exchange(id='string', card_token_request=shared.CardTokenRequest(
    verification_code='string',
    verification_token='string',
))

if res.card_token_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `id`                                                                         | *str*                                                                        | :heavy_check_mark:                                                           | Unique identifier                                                            |
| `card_token_request`                                                         | [Optional[shared.CardTokenRequest]](../../models/shared/cardtokenrequest.md) | :heavy_minus_sign:                                                           | N/A                                                                          |


### Response

**[operations.ExchangeCodeToTokenResponse](../../models/operations/exchangecodetotokenresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

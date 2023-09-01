# code_to_token

### Available Operations

* [exchange](#exchange) - Exchange the code for a token

## exchange

Exchange the code for a token

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()

req = operations.ExchangeCodeToTokenRequest(
    card_token_request=shared.CardTokenRequest(
        verification_code='vero',
        verification_token='nihil',
    ),
    id='8f097b00-74f1-4547-9b5e-6e13b99d488e',
)

res = s.code_to_token.exchange(req)

if res.card_token_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ExchangeCodeToTokenRequest](../../models/operations/exchangecodetotokenrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.ExchangeCodeToTokenResponse](../../models/operations/exchangecodetotokenresponse.md)**


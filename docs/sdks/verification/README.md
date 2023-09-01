# verification

### Available Operations

* [send](#send) - Sends a verification code

## send

Sends a verification code

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()

req = operations.SendVerificationRequest(
    card_code_request=shared.CardCodeRequest(
        channel='rerum',
    ),
    id='3fe49a8d-9cbf-4486-b332-3f9b77f3a410',
)

res = s.verification.send(req)

if res.card_code_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.SendVerificationRequest](../../models/operations/sendverificationrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.SendVerificationResponse](../../models/operations/sendverificationresponse.md)**


# Verification
(*verification*)

### Available Operations

* [send](#send) - Sends a verification code

## send

Sends a verification code

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()


res = s.verification.send(id='string', card_code_request=shared.CardCodeRequest(
    channel='string',
))

if res.card_code_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `id`                                                                       | *str*                                                                      | :heavy_check_mark:                                                         | Unique identifier                                                          |
| `card_code_request`                                                        | [Optional[shared.CardCodeRequest]](../../models/shared/cardcoderequest.md) | :heavy_minus_sign:                                                         | N/A                                                                        |


### Response

**[operations.SendVerificationResponse](../../models/operations/sendverificationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

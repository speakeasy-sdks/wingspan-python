# one_thousand_and_ninety_nine

### Available Operations

* [mark](#mark) - Mark a 1099 submission as returned by mail for collaborator

## mark

Mark a 1099 submission as returned by mail for collaborator

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()

req = shared.Mark1099AsUndeliveredRequest(
    member_id='quibusdam',
    submission_index=6027.63,
    year=8579.46,
)

res = s.one_thousand_and_ninety_nine.mark(req)

if res.mark1099_as_undelivered_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [shared.Mark1099AsUndeliveredRequest](../../models/shared/mark1099asundeliveredrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.Mark1099Response](../../models/operations/mark1099response.md)**


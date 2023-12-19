# OneThousandAndNinetyNine
(*one_thousand_and_ninety_nine*)

### Available Operations

* [calculate](#calculate) - Calculate 1099 amounts for collaborator
* [mark](#mark) - Mark a 1099 submission as returned by mail for collaborator
* [remail](#remail) - Re-mail 1099 submission for collaborator

## calculate

Calculate 1099 amounts for collaborator

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()

req = shared.Calculate1099Request(
    member_client_id='string',
    year=6611.96,
)

res = s.one_thousand_and_ninety_nine.calculate(req)

if res.calculate1099_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [shared.Calculate1099Request](../../models/shared/calculate1099request.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.Calculate1099Response](../../models/operations/calculate1099response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## mark

Mark a 1099 submission as returned by mail for collaborator

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()

req = shared.Mark1099AsUndeliveredRequest(
    member_id='string',
    submission_index=2694.09,
    year=735.52,
)

res = s.one_thousand_and_ninety_nine.mark(req)

if res.mark1099_as_undelivered_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [shared.Mark1099AsUndeliveredRequest](../../models/shared/mark1099asundeliveredrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.Mark1099Response](../../models/operations/mark1099response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remail

Re-mail 1099 submission for collaborator

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()

req = shared.Remail1099Request(
    address=shared.Sevenb49dbbd81f36ab6d7b4f07c5e2e53f40e36eb7b83d1488f379e993b830eec56(
        address_line1='string',
        city='Port Cara',
        postal_code='13281-2223',
        state='string',
    ),
    member_id='string',
    year=3145.26,
)

res = s.one_thousand_and_ninety_nine.remail(req)

if res.remail1099_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [shared.Remail1099Request](../../models/shared/remail1099request.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.Remail1099Response](../../models/operations/remail1099response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

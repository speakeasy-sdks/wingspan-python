# statement

### Available Operations

* [download](#download) - Download bank statement pdf
* [get](#get) - Get bank statement

## download

Download bank statement pdf

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()

req = operations.DownloadStatementRequest(
    id='028921cd-dc69-4260-9fb5-76b0d5f0d30c',
)

res = s.statement.download(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.DownloadStatementRequest](../../models/operations/downloadstatementrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.DownloadStatementResponse](../../models/operations/downloadstatementresponse.md)**


## get

Get bank statement

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()

req = operations.GetStatementRequest(
    id='5fbb2587-0532-402c-b3d5-fe9b90c28909',
)

res = s.statement.get(req)

if res.bank_statements is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetStatementRequest](../../models/operations/getstatementrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.GetStatementResponse](../../models/operations/getstatementresponse.md)**


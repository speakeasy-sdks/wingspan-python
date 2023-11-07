# Statement
(*.statement*)

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


res = s.statement.download(id='string')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.DownloadStatementResponse](../../models/operations/downloadstatementresponse.md)**


## get

Get bank statement

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.statement.get(id='string')

if res.classes is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.GetStatementResponse](../../models/operations/getstatementresponse.md)**


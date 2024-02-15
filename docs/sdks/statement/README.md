# Statement
(*statement*)

### Available Operations

* [download](#download) - Download bank statement pdf
* [get](#get) - Get bank statement

## download

Download bank statement pdf

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.statement.download(id='<value>')

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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get

Get bank statement

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.statement.get(id='<value>')

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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

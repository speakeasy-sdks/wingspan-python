# Form1099
(*form1099*)

### Available Operations

* [download](#download) - Downloads a form 1099 PDF for a collaborator

## download

Downloads a form 1099 PDF for a collaborator

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.form1099.download(id='string', index='string', year='string')

if res.download1099_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |
| `index`            | *str*              | :heavy_check_mark: | Index              |
| `year`             | *str*              | :heavy_check_mark: | Year               |


### Response

**[operations.DownloadForm1099Response](../../models/operations/downloadform1099response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

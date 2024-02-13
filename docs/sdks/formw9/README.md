# FormW9
(*form_w9*)

### Available Operations

* [download](#download) - Downloads a form W9 PDF for a collaborator

## download

Downloads a form W9 PDF for a collaborator

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.form_w9.download(id='string')

if res.download_w9_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.DownloadFormW9Response](../../models/operations/downloadformw9response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

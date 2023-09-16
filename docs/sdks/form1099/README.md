# Form1099

### Available Operations

* [download](#download) - Downloads a form 1099 PDF for a collaborator

## download

Downloads a form 1099 PDF for a collaborator

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.form1099.download(id='sunt', index='ullam', year='nam')

if res.download1099_response is not None:
    # handle response
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |
| `index`            | *str*              | :heavy_check_mark: | Index              |
| `year`             | *str*              | :heavy_check_mark: | Year               |


### Response

**[operations.DownloadForm1099Response](../../models/operations/downloadform1099response.md)**


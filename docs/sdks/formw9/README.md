# form_w9

### Available Operations

* [download](#download) - Downloads a form W9 PDF for a collaborator

## download

Downloads a form W9 PDF for a collaborator

### Example Usage

```python
import petstore
from petstore.models import operations

s = petstore.Petstore()

req = operations.DownloadFormW9Request(
    id='63c969e9-a3ef-4a77-9fb1-4cd66ae395ef',
)

res = s.form_w9.download(req)

if res.download_w9_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.DownloadFormW9Request](../../models/operations/downloadformw9request.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.DownloadFormW9Response](../../models/operations/downloadformw9response.md)**


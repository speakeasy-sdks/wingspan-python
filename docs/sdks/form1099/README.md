# form1099

### Available Operations

* [download](#download) - Downloads a form 1099 PDF for a collaborator

## download

Downloads a form 1099 PDF for a collaborator

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()

req = operations.DownloadForm1099Request(
    id='1e91e450-ad2a-4bd4-8269-802d502a94bb',
    index='labore',
    year='delectus',
)

res = s.form1099.download(req)

if res.download1099_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.DownloadForm1099Request](../../models/operations/downloadform1099request.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.DownloadForm1099Response](../../models/operations/downloadform1099response.md)**


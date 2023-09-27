# Institution
(*institution*)

### Available Operations

* [get](#get) - Get Institution By Routing Number

## get

Get Institution By Routing Number

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.institution.get(routing_number='voluptatem')

if res.institution_response is not None:
    # handle response
```

### Parameters

| Parameter           | Type                | Required            | Description         |
| ------------------- | ------------------- | ------------------- | ------------------- |
| `routing_number`    | *str*               | :heavy_check_mark:  | Bank Routing Number |


### Response

**[operations.GetInstitutionResponse](../../models/operations/getinstitutionresponse.md)**


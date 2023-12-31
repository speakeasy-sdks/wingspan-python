# BulkPayableBatchSummary
(*bulk_payable_batch_summary*)

### Available Operations

* [get](#get) - Get Bulk Payable Batch Import Summary

## get

Get Bulk Payable Batch Import Summary

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.bulk_payable_batch_summary.get(batch_id='female')

if res.bulk_payable_import_summary is not None:
    # handle response
    pass
```

### Parameters

| Parameter                     | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `batch_id`                    | *str*                         | :heavy_check_mark:            | Unique identifier for a batch |


### Response

**[operations.GetBulkPayableBatchSummaryResponse](../../models/operations/getbulkpayablebatchsummaryresponse.md)**


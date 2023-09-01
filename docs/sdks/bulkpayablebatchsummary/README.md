# bulk_payable_batch_summary

### Available Operations

* [get](#get) - Get Bulk Payable Batch Import Summary

## get

Get Bulk Payable Batch Import Summary

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()

req = operations.GetBulkPayableBatchSummaryRequest(
    batch_id='hic',
)

res = s.bulk_payable_batch_summary.get(req)

if res.bulk_payable_import_summary is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetBulkPayableBatchSummaryRequest](../../models/operations/getbulkpayablebatchsummaryrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.GetBulkPayableBatchSummaryResponse](../../models/operations/getbulkpayablebatchsummaryresponse.md)**


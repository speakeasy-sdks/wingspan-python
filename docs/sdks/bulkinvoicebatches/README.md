# BulkInvoiceBatches
(*.bulk_invoice_batches*)

### Available Operations

* [list](#list) - List bulk invoice batches

## list

List bulk invoice batches

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.bulk_invoice_batches.list()

if res.classes is not None:
    # handle response
    pass
```


### Response

**[operations.ListBulkInvoiceBatchesResponse](../../models/operations/listbulkinvoicebatchesresponse.md)**


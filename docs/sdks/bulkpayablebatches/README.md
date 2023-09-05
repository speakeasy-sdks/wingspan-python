# bulk_payable_batches

### Available Operations

* [list](#list) - List bulk payable batches

## list

List bulk payable batches

### Example Usage

```python
import wingspan


s = wingspan.Wingspan()


res = s.bulk_payable_batches.list()

if res.bulk_payable_batches is not None:
    # handle response
```


### Response

**[operations.ListBulkPayableBatchesResponse](../../models/operations/listbulkpayablebatchesresponse.md)**


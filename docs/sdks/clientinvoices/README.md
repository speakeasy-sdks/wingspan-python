# client_invoices

### Available Operations

* [list](#list) - List invoices on client

## list

List invoices on client

### Example Usage

```python
import wingspan


s = wingspan.Wingspan()


res = s.client_invoices.list()

if res.payable_schemas is not None:
    # handle response
```


### Response

**[operations.ListClientInvoicesResponse](../../models/operations/listclientinvoicesresponse.md)**


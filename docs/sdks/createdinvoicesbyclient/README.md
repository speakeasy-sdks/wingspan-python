# CreatedInvoicesByClient
(*created_invoices_by_client*)

### Available Operations

* [list](#list) - List invoices created by client

## list

List invoices created by client

### Example Usage

```python
import wingspan


s = wingspan.Wingspan()


res = s.created_invoices_by_client.list()

if res.client_invoices is not None:
    # handle response
    pass
```


### Response

**[operations.ListCreatedInvoicesByClientResponse](../../models/operations/listcreatedinvoicesbyclientresponse.md)**


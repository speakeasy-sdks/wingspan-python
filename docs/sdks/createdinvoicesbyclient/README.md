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

if res.classes is not None:
    # handle response
    pass

```


### Response

**[operations.ListCreatedInvoicesByClientResponse](../../models/operations/listcreatedinvoicesbyclientresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

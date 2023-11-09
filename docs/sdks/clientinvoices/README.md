# ClientInvoices
(*client_invoices*)

### Available Operations

* [list](#list) - List invoices on client

## list

List invoices on client

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.client_invoices.list()

if res.classes is not None:
    # handle response
    pass
```


### Response

**[operations.ListClientInvoicesResponse](../../models/operations/listclientinvoicesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

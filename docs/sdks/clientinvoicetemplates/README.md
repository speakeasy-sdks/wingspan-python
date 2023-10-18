# ClientInvoiceTemplates
(*client_invoice_templates*)

### Available Operations

* [list](#list) - List client-invoice-templates

## list

List client-invoice-templates

### Example Usage

```python
import wingspan


s = wingspan.Wingspan()


res = s.client_invoice_templates.list()

if res.client_invoice_templates is not None:
    # handle response
    pass
```


### Response

**[operations.ListClientInvoiceTemplatesResponse](../../models/operations/listclientinvoicetemplatesresponse.md)**


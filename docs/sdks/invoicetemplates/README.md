# InvoiceTemplates

### Available Operations

* [list](#list) - List invoiceTemplates

## list

List invoiceTemplates

### Example Usage

```python
import wingspan


s = wingspan.Wingspan()


res = s.invoice_templates.list()

if res.invoice_templates is not None:
    # handle response
```


### Response

**[operations.ListInvoiceTemplatesResponse](../../models/operations/listinvoicetemplatesresponse.md)**


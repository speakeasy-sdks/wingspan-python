# InvoiceTemplates
(*invoice_templates*)

### Available Operations

* [list](#list) - List invoiceTemplates

## list

List invoiceTemplates

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.invoice_templates.list()

if res.classes is not None:
    # handle response
    pass
```


### Response

**[operations.ListInvoiceTemplatesResponse](../../models/operations/listinvoicetemplatesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

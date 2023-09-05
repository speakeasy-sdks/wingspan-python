# member_invoices

### Available Operations

* [list](#list) - List invoices on member

## list

List invoices on member

### Example Usage

```python
import wingspan


s = wingspan.Wingspan()


res = s.member_invoices.list()

if res.invoices is not None:
    # handle response
```


### Response

**[operations.ListMemberInvoicesResponse](../../models/operations/listmemberinvoicesresponse.md)**


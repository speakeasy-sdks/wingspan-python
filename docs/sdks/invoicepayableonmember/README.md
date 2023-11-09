# InvoicePayableOnMember
(*invoice_payable_on_member*)

### Available Operations

* [get](#get) - Get invoice on member by payableId

## get

Get invoice on member by payableId

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.invoice_payable_on_member.get(id='string')

if res.payable_schema is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.GetInvoicePayableOnMemberResponse](../../models/operations/getinvoicepayableonmemberresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

# PaPayableOnClientyable
(*pa_payable_on_clientyable*)

### Available Operations

* [delete](#delete) - Delete payable on client by payableId

## delete

Delete payable on client by payableId

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.pa_payable_on_clientyable.delete(id='<value>')

if res.payable_schema is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.DeletePayableOnClientResponse](../../models/operations/deletepayableonclientresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

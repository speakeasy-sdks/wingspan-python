# BankStatements
(*bank_statements*)

### Available Operations

* [list](#list) - List bank statements

## list

List bank statements

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.bank_statements.list()

if res.classes is not None:
    # handle response
    pass
```


### Response

**[operations.ListBankStatementsResponse](../../models/operations/listbankstatementsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

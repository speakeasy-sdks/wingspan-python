# bank_statements

### Available Operations

* [list](#list) - List bank statements

## list

List bank statements

### Example Usage

```python
import wingspan


s = wingspan.Wingspan()


res = s.bank_statements.list()

if res.bank_statements is not None:
    # handle response
```


### Response

**[operations.ListBankStatementsResponse](../../models/operations/listbankstatementsresponse.md)**


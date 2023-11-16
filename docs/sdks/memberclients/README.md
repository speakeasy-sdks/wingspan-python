# MemberClients
(*member_clients*)

### Available Operations

* [list](#list) - List memberClients

## list

List memberClients

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.member_clients.list()

if res.classes is not None:
    # handle response
    pass
```


### Response

**[operations.ListMemberClientsResponse](../../models/operations/listmemberclientsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

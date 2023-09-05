# member_clients

### Available Operations

* [list](#list) - List memberClients

## list

List memberClients

### Example Usage

```python
import wingspan


s = wingspan.Wingspan()


res = s.member_clients.list()

if res.member_client_schemas is not None:
    # handle response
```


### Response

**[operations.ListMemberClientsResponse](../../models/operations/listmemberclientsresponse.md)**


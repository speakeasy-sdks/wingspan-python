# Cards
(*cards*)

### Available Operations

* [list](#list) - List cards

## list

List cards

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.cards.list()

if res.classes is not None:
    # handle response
    pass

```


### Response

**[operations.ListCardsResponse](../../models/operations/listcardsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

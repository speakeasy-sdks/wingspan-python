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

if res.cards is not None:
    # handle response
    pass
```


### Response

**[operations.ListCardsResponse](../../models/operations/listcardsresponse.md)**


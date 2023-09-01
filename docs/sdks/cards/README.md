# cards

### Available Operations

* [list](#list) - List cards

## list

List cards

### Example Usage

```python
import petstore


s = petstore.Petstore()


res = s.cards.list()

if res.cards is not None:
    # handle response
```


### Response

**[operations.ListCardsResponse](../../models/operations/listcardsresponse.md)**


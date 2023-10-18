# LineItemsAgingGroup
(*line_items_aging_group*)

### Available Operations

* [get](#get) - Get a list of line items with respective aging group

## get

Get a list of line items with respective aging group

### Example Usage

```python
import wingspan


s = wingspan.Wingspan()


res = s.line_items_aging_group.get()

if res.line_items_aging_report_responses is not None:
    # handle response
    pass
```


### Response

**[operations.GetLineItemsAgingGroupResponse](../../models/operations/getlineitemsaginggroupresponse.md)**


# additional_settings

### Available Operations

* [list](#list) - List additional settings

## list

List additional settings

### Example Usage

```python
import wingspan


s = wingspan.Wingspan()


res = s.additional_settings.list()

if res.additional_data is not None:
    # handle response
```


### Response

**[operations.ListAdditionalSettingsResponse](../../models/operations/listadditionalsettingsresponse.md)**


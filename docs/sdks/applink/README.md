# AppLink
(*app_link*)

### Available Operations

* [get](#get) - Gets an application link for creating the clearing bank account

## get

Gets an application link for creating the clearing bank account

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.app_link.get(member_id='<value>')

if res.banking_application_form is not None:
    # handle response
    pass

```

### Parameters

| Parameter                     | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `member_id`                   | *str*                         | :heavy_check_mark:            | Unique identifier of a member |


### Response

**[operations.GetAppLinkResponse](../../models/operations/getapplinkresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

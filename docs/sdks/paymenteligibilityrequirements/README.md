# PaymentEligibilityRequirements
(*payment_eligibility_requirements*)

### Available Operations

* [list](#list) - List Payment Eligigbility Requirements

## list

List Payment Eligigbility Requirements

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.payment_eligibility_requirements.list()

if res.classes is not None:
    # handle response
    pass
```


### Response

**[operations.ListPaymentEligibilityRequirementsResponse](../../models/operations/listpaymenteligibilityrequirementsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

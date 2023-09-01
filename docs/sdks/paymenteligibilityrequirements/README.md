# payment_eligibility_requirements

### Available Operations

* [list](#list) - List Payment Eligigbility Requirements

## list

List Payment Eligigbility Requirements

### Example Usage

```python
import wingspan


s = wingspan.Wingspan()


res = s.payment_eligibility_requirements.list()

if res.payment_eligibilities is not None:
    # handle response
```


### Response

**[operations.ListPaymentEligibilityRequirementsResponse](../../models/operations/listpaymenteligibilityrequirementsresponse.md)**

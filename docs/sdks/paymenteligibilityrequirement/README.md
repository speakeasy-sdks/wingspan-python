# payment_eligibility_requirement

### Available Operations

* [create](#create) - Create Payment Eligibility Requirement
* [delete](#delete) - Delete Payment Eligibility Requirement
* [get](#get) - Get Payment Eligibility Requirement

## create

Create Payment Eligibility Requirement

### Example Usage

```python
import petstore
from petstore.models import shared

s = petstore.Petstore()

req = shared.PaymentEligibility(
    field='provident',
    value='nam',
)

res = s.payment_eligibility_requirement.create(req)

if res.payment_eligibility is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [shared.PaymentEligibility](../../models/shared/paymenteligibility.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.CreatePaymentEligibilityRequirementResponse](../../models/operations/createpaymenteligibilityrequirementresponse.md)**


## delete

Delete Payment Eligibility Requirement

### Example Usage

```python
import petstore
from petstore.models import operations

s = petstore.Petstore()

req = operations.DeletePaymentEligibilityRequirementRequest(
    id='a88f3a66-9970-474b-a446-9b6e21419598',
)

res = s.payment_eligibility_requirement.delete(req)

if res.payment_eligibility is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.DeletePaymentEligibilityRequirementRequest](../../models/operations/deletepaymenteligibilityrequirementrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |


### Response

**[operations.DeletePaymentEligibilityRequirementResponse](../../models/operations/deletepaymenteligibilityrequirementresponse.md)**


## get

Get Payment Eligibility Requirement

### Example Usage

```python
import petstore
from petstore.models import operations

s = petstore.Petstore()

req = operations.GetPaymentEligibilityRequirementRequest(
    id='90afa563-e251-46fe-8c8b-711e5b7fd2ed',
)

res = s.payment_eligibility_requirement.get(req)

if res.payment_eligibility is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.GetPaymentEligibilityRequirementRequest](../../models/operations/getpaymenteligibilityrequirementrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.GetPaymentEligibilityRequirementResponse](../../models/operations/getpaymenteligibilityrequirementresponse.md)**


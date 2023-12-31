# PaymentEligibilityRequirement
(*payment_eligibility_requirement*)

### Available Operations

* [create](#create) - Create Payment Eligibility Requirement
* [delete](#delete) - Delete Payment Eligibility Requirement
* [get](#get) - Get Payment Eligibility Requirement
* [update](#update) - Update Payment Eligibility Requirement

## create

Create Payment Eligibility Requirement

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()

req = shared.PaymentEligibility(
    field='online',
    value='Configuration',
)

res = s.payment_eligibility_requirement.create(req)

if res.payment_eligibility is not None:
    # handle response
    pass
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
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.payment_eligibility_requirement.delete(id='program')

if res.payment_eligibility is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.DeletePaymentEligibilityRequirementResponse](../../models/operations/deletepaymenteligibilityrequirementresponse.md)**


## get

Get Payment Eligibility Requirement

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.payment_eligibility_requirement.get(id='female')

if res.payment_eligibility is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.GetPaymentEligibilityRequirementResponse](../../models/operations/getpaymenteligibilityrequirementresponse.md)**


## update

Update Payment Eligibility Requirement

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()


res = s.payment_eligibility_requirement.update(id='Van', payment_eligibility_update_request=shared.PaymentEligibilityUpdateRequest(
    value=shared.PaymentEligibilityUpdateRequestValue(),
))

if res.payment_eligibility is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                       | *str*                                                                                                      | :heavy_check_mark:                                                                                         | Unique identifier                                                                                          |
| `payment_eligibility_update_request`                                                                       | [Optional[shared.PaymentEligibilityUpdateRequest]](../../models/shared/paymenteligibilityupdaterequest.md) | :heavy_minus_sign:                                                                                         | N/A                                                                                                        |


### Response

**[operations.UpdatePaymentEligibilityRequirementResponse](../../models/operations/updatepaymenteligibilityrequirementresponse.md)**


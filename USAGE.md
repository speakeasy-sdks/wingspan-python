<!-- Start SDK Example Usage -->


```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()

req = operations.DeletePaymentsBankingCardIDRequest(
    id='89bd9d8d-69a6-474e-8f46-7cc8796ed151',
)

res = s.delete_payments_banking_card_id_(req)

if res.card is not None:
    # handle response
```
<!-- End SDK Example Usage -->
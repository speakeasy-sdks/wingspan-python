<!-- Start SDK Example Usage -->


```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()

req = shared.Calculate1099Request(
    member_client_id='corrupti',
    year=5928.45,
)

res = s.one_thousand_and_ninety_nine.calculate(req)

if res.calculate1099_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->
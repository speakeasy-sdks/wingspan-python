<!-- Start SDK Example Usage -->


```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()

req = shared.Calculate1099Request(
    member_client_id='string',
    year=6611.96,
)

res = s.one_thousand_and_ninety_nine.calculate(req)

if res.calculate1099_response is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->
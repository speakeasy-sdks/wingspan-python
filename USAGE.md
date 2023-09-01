<!-- Start SDK Example Usage -->


```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()

req = shared.Mark1099AsUndeliveredRequest(
    member_id='corrupti',
    submission_index=5928.45,
    year=7151.9,
)

res = s.one_thousand_and_ninety_nine.mark(req)

if res.mark1099_as_undelivered_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->
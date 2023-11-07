<!-- Start SDK Example Usage -->


```python
import wingspan

s = wingspan.Wingspan()


res = s.service_status.get()

if res.ping is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->
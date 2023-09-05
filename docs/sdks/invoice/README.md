# invoice

### Available Operations

* [generate](#generate) - Generate invoice
* [send](#send) - Send invoice

## generate

Generate invoice

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.invoice.generate(invoice_id='tempora')

if res.invoice_pdf_generation_response is not None:
    # handle response
```

### Parameters

| Parameter                       | Type                            | Required                        | Description                     |
| ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| `invoice_id`                    | *str*                           | :heavy_check_mark:              | Unique identifier of an invoice |


### Response

**[operations.GenerateInvoiceResponse](../../models/operations/generateinvoiceresponse.md)**


## send

Send invoice

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.invoice.send(invoice_id='debitis')

if res.invoice is not None:
    # handle response
```

### Parameters

| Parameter                       | Type                            | Required                        | Description                     |
| ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| `invoice_id`                    | *str*                           | :heavy_check_mark:              | Unique identifier of an invoice |


### Response

**[operations.SendInvoiceResponse](../../models/operations/sendinvoiceresponse.md)**


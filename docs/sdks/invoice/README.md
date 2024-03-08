# Invoice
(*invoice*)

### Available Operations

* [generate](#generate) - Generate invoice
* [send](#send) - Send invoice

## generate

Generate invoice

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.invoice.generate(invoice_id='<value>')

if res.invoice_pdf_generation_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                       | Type                            | Required                        | Description                     |
| ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| `invoice_id`                    | *str*                           | :heavy_check_mark:              | Unique identifier of an invoice |


### Response

**[operations.GenerateInvoiceResponse](../../models/operations/generateinvoiceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## send

Send invoice

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.invoice.send(invoice_id='<value>')

if res.invoice is not None:
    # handle response
    pass

```

### Parameters

| Parameter                       | Type                            | Required                        | Description                     |
| ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| `invoice_id`                    | *str*                           | :heavy_check_mark:              | Unique identifier of an invoice |


### Response

**[operations.SendInvoiceResponse](../../models/operations/sendinvoiceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

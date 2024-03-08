# InvoiceTemplate
(*invoice_template*)

### Available Operations

* [create](#create) - Create invoice-template
* [delete](#delete) - Delete invoice-template
* [get](#get) - Get invoice-template
* [update](#update) - Update invoice-template

## create

Create invoice-template

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()

req = shared.InvoiceTemplateCreateRequest(
    invoice_data=shared.InvoiceDataCreateRequest(
        line_items=[
            shared.InvoiceLineItemsCreateRequest(),
        ],
        member_client_id='<value>',
    ),
    status=shared.StatusInvoiceTemplateCreateRequest.DRAFT,
)

res = s.invoice_template.create(req)

if res.invoice_template is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [shared.InvoiceTemplateCreateRequest](../../models/shared/invoicetemplatecreaterequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.CreateInvoiceTemplateResponse](../../models/operations/createinvoicetemplateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete

Delete invoice-template

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.invoice_template.delete(id='<value>')

if res.invoice_template is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.DeleteInvoiceTemplateResponse](../../models/operations/deleteinvoicetemplateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get

Get invoice-template

### Example Usage

```python
import wingspan

s = wingspan.Wingspan()


res = s.invoice_template.get(id='<value>')

if res.invoice_template is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.GetInvoiceTemplateResponse](../../models/operations/getinvoicetemplateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update

Update invoice-template

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()


res = s.invoice_template.update(id='<value>', invoice_template_update_request=shared.InvoiceTemplateUpdateRequest())

if res.invoice_template is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `id`                                                                                                 | *str*                                                                                                | :heavy_check_mark:                                                                                   | Unique identifier                                                                                    |
| `invoice_template_update_request`                                                                    | [Optional[shared.InvoiceTemplateUpdateRequest]](../../models/shared/invoicetemplateupdaterequest.md) | :heavy_minus_sign:                                                                                   | N/A                                                                                                  |


### Response

**[operations.UpdateInvoiceTemplateResponse](../../models/operations/updateinvoicetemplateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

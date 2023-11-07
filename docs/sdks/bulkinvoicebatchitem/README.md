# BulkInvoiceBatchItem
(*.bulk_invoice_batch_item*)

### Available Operations

* [create](#create) - Create a bulk invoice batch item
* [get](#get) - Get a bulk invoice batch item
* [update](#update) - Update a bulk invoice batch item

## create

Create a bulk invoice batch item

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()


res = s.bulk_invoice_batch_item.create(batch_id='string', bulk_invoice_item_create=shared.BulkInvoiceItemCreate(
    accepted_payment_methods=[
        shared.BulkInvoiceItemCreateAcceptedPaymentMethods.ACH,
    ],
    amount=4893.82,
    bulk_invoice_batch_id='string',
    credit_fee_handling=shared.FeeHandlingConfig(),
    due_date='string',
    invoice_status=shared.InvoiceStatusBulkInvoiceItemCreate.PAID,
    labels={
        "key": 'string',
    },
    line_item_description='string',
))

if res.bulk_invoice_item is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `batch_id`                                                                             | *str*                                                                                  | :heavy_check_mark:                                                                     | Unique identifier for a batch                                                          |
| `bulk_invoice_item_create`                                                             | [Optional[shared.BulkInvoiceItemCreate]](../../models/shared/bulkinvoiceitemcreate.md) | :heavy_minus_sign:                                                                     | N/A                                                                                    |


### Response

**[operations.CreateBulkInvoiceBatchItemResponse](../../models/operations/createbulkinvoicebatchitemresponse.md)**


## get

Get a bulk invoice batch item

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()


res = s.bulk_invoice_batch_item.get(batch_id='string', batch_item_id='string')

if res.bulk_invoice_item is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                | Type                                     | Required                                 | Description                              |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `batch_id`                               | *str*                                    | :heavy_check_mark:                       | Unique identifier for a batch            |
| `batch_item_id`                          | *str*                                    | :heavy_check_mark:                       | Unique identifier for an item in a batch |


### Response

**[operations.GetBulkInvoiceBatchItemResponse](../../models/operations/getbulkinvoicebatchitemresponse.md)**


## update

Update a bulk invoice batch item

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()


res = s.bulk_invoice_batch_item.update(batch_id='string', batch_item_id='string', bulk_invoice_item_update=shared.BulkInvoiceItemUpdate(
    accepted_payment_methods=[
        shared.BulkInvoiceItemUpdateAcceptedPaymentMethods.LESS_THAN_NIL_GREATER_THAN_,
    ],
    credit_fee_handling=shared.FeeHandlingConfig(),
    labels={
        "key": 'string',
    },
))

if res.bulk_invoice_item is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `batch_id`                                                                             | *str*                                                                                  | :heavy_check_mark:                                                                     | Unique identifier for a batch                                                          |
| `batch_item_id`                                                                        | *str*                                                                                  | :heavy_check_mark:                                                                     | Unique identifier for an item in a batch                                               |
| `bulk_invoice_item_update`                                                             | [Optional[shared.BulkInvoiceItemUpdate]](../../models/shared/bulkinvoiceitemupdate.md) | :heavy_minus_sign:                                                                     | N/A                                                                                    |


### Response

**[operations.UpdateBulkInvoiceBatchItemResponse](../../models/operations/updatebulkinvoicebatchitemresponse.md)**


# BulkInvoiceBatchItem
(*bulk_invoice_batch_item*)

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


res = s.bulk_invoice_batch_item.create(batch_id='aut', bulk_invoice_item_create=shared.BulkInvoiceItemCreate(
    accepted_payment_methods=[
        shared.BulkInvoiceItemCreateAcceptedPaymentMethods.CREDIT,
    ],
    amount=6228.46,
    bulk_invoice_batch_id='temporibus',
    bulk_invoice_item_merge_key='laborum',
    bulk_invoice_item_reference='quasi',
    client_email='reiciendis',
    client_external_id='voluptatibus',
    credit_fee_handling=[],
    due_date='vero',
    invoice_notes='nihil',
    invoice_status=shared.InvoiceStatusBulkInvoiceItemCreate.APPROVED,
    labels=[],
    line_item_description='voluptatibus',
    line_item_detail='ipsa',
    member_client_id='omnis',
    paid_date='voluptate',
    project_name='cum',
    reimbursable_expense=[],
    send_date='perferendis',
))

if res.bulk_invoice_item is not None:
    # handle response
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


res = s.bulk_invoice_batch_item.get(batch_id='doloremque', batch_item_id='reprehenderit')

if res.bulk_invoice_item is not None:
    # handle response
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


res = s.bulk_invoice_batch_item.update(batch_id='ut', batch_item_id='maiores', bulk_invoice_item_update=shared.BulkInvoiceItemUpdate(
    accepted_payment_methods=[
        shared.BulkInvoiceItemUpdateAcceptedPaymentMethods.CREDIT,
    ],
    amount=3594.44,
    bulk_invoice_batch_id='dolore',
    bulk_invoice_item_merge_key='iusto',
    bulk_invoice_item_reference='dicta',
    client_email='harum',
    client_external_id='enim',
    credit_fee_handling=[],
    due_date='accusamus',
    invoice_notes='commodi',
    invoice_status=shared.InvoiceStatusBulkInvoiceItemUpdate.LESS_THAN_NIL_GREATER_THAN_,
    labels=[],
    line_item_description='quae',
    line_item_detail='ipsum',
    member_client_id='quidem',
    paid_date='molestias',
    project_name='excepturi',
    reimbursable_expense=[],
    send_date='pariatur',
))

if res.bulk_invoice_item is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `batch_id`                                                                             | *str*                                                                                  | :heavy_check_mark:                                                                     | Unique identifier for a batch                                                          |
| `batch_item_id`                                                                        | *str*                                                                                  | :heavy_check_mark:                                                                     | Unique identifier for an item in a batch                                               |
| `bulk_invoice_item_update`                                                             | [Optional[shared.BulkInvoiceItemUpdate]](../../models/shared/bulkinvoiceitemupdate.md) | :heavy_minus_sign:                                                                     | N/A                                                                                    |


### Response

**[operations.UpdateBulkInvoiceBatchItemResponse](../../models/operations/updatebulkinvoicebatchitemresponse.md)**


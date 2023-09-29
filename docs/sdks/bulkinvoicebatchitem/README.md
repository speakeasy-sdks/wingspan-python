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


res = s.bulk_invoice_batch_item.create(batch_id='online', bulk_invoice_item_create=shared.BulkInvoiceItemCreate(
    accepted_payment_methods=[
        shared.BulkInvoiceItemCreateAcceptedPaymentMethods.MANUAL,
    ],
    amount=8592.13,
    bulk_invoice_batch_id='innovative blue',
    bulk_invoice_item_merge_key='grey technology East',
    bulk_invoice_item_reference='evolve',
    client_email='fuchsia Gasoline Screen',
    client_external_id='physical Ameliorated',
    credit_fee_handling=[],
    due_date='after',
    invoice_notes='Intelligent Fish',
    invoice_status=shared.InvoiceStatusBulkInvoiceItemCreate.DRAFT,
    labels=[],
    line_item_description='functionalities Grocery Borders',
    line_item_detail='Profound',
    member_client_id='metrics',
    paid_date='Minivan',
    project_name='Senior Mouse West',
    reimbursable_expense=[],
    send_date='Towels likewise',
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


res = s.bulk_invoice_batch_item.get(batch_id='female', batch_item_id='program')

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


res = s.bulk_invoice_batch_item.update(batch_id='Van', batch_item_id='East', bulk_invoice_item_update=shared.BulkInvoiceItemUpdate(
    accepted_payment_methods=[
        shared.BulkInvoiceItemUpdateAcceptedPaymentMethods.MANUAL,
    ],
    amount=9914.64,
    bulk_invoice_batch_id='Quality',
    bulk_invoice_item_merge_key='invoice Arizona',
    bulk_invoice_item_reference='mostly',
    client_email='dynamic white',
    client_external_id='Carolina syndicate',
    credit_fee_handling=[],
    due_date='implement JBOD',
    invoice_notes='Quality guestbook driver',
    invoice_status=shared.InvoiceStatusBulkInvoiceItemUpdate.APPROVED,
    labels=[],
    line_item_description='Sharable Division Northeast',
    line_item_detail='Northwest Fantastic',
    member_client_id='Internal invoice',
    paid_date='brightly',
    project_name='frictionless haptic modulo',
    reimbursable_expense=[],
    send_date='navigating Diesel Avon',
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


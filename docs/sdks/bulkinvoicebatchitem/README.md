# BulkInvoiceBatchItem

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


res = s.bulk_invoice_batch_item.create(batch_id='tempora', bulk_invoice_item_create=shared.BulkInvoiceItemCreate(
    accepted_payment_methods=[
        shared.BulkInvoiceItemCreateAcceptedPaymentMethods.MANUAL,
    ],
    amount=7351.94,
    bulk_invoice_batch_id='labore',
    bulk_invoice_item_merge_key='delectus',
    bulk_invoice_item_reference='eum',
    client_email='non',
    client_external_id='eligendi',
    credit_fee_handling=shared.FeeHandlingConfig(
        client_absolute_percentage=3960.98,
        client_pays=5920.42,
        member_pays=8960.39,
    ),
    due_date='sint',
    invoice_notes='officia',
    invoice_status=shared.InvoiceStatusBulkInvoiceItemCreate.OPEN,
    labels={
        "a": 'dolorum',
    },
    line_item_description='in',
    line_item_detail='in',
    member_client_id='illum',
    paid_date='maiores',
    project_name='rerum',
    reimbursable_expense='magnam',
    send_date='cumque',
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


res = s.bulk_invoice_batch_item.get(batch_id='facere', batch_item_id='ea')

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


res = s.bulk_invoice_batch_item.update(batch_id='aliquid', batch_item_id='laborum', bulk_invoice_item_update=shared.BulkInvoiceItemUpdate(
    accepted_payment_methods=[
        shared.BulkInvoiceItemUpdateAcceptedPaymentMethods.LESS_THAN_NIL_GREATER_THAN_,
    ],
    amount=2497.96,
    bulk_invoice_batch_id='occaecati',
    bulk_invoice_item_merge_key='enim',
    bulk_invoice_item_reference='accusamus',
    client_email='delectus',
    client_external_id='quidem',
    credit_fee_handling=shared.FeeHandlingConfig(
        client_absolute_percentage=7252.55,
        client_pays=6596.69,
        member_pays=5013.24,
    ),
    due_date='deleniti',
    invoice_notes='sapiente',
    invoice_status=shared.InvoiceStatusBulkInvoiceItemUpdate.OPEN,
    labels={
        "nisi": 'vel',
    },
    line_item_description='natus',
    line_item_detail='omnis',
    member_client_id='molestiae',
    paid_date='perferendis',
    project_name='nihil',
    reimbursable_expense='distinctio',
    send_date='id',
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


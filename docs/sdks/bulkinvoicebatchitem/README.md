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


res = s.bulk_invoice_batch_item.create(batch_id='alias', bulk_invoice_item_create=shared.BulkInvoiceItemCreate(
    accepted_payment_methods=[
        shared.BulkInvoiceItemCreateAcceptedPaymentMethods.CREDIT,
    ],
    amount=6778.17,
    bulk_invoice_batch_id='excepturi',
    bulk_invoice_item_merge_key='tempora',
    bulk_invoice_item_reference='facilis',
    client_email='tempore',
    client_external_id='labore',
    credit_fee_handling=shared.FeeHandlingConfig(
        client_absolute_percentage=4332.88,
        client_pays=2487.53,
        member_pays=7561.07,
    ),
    due_date='sint',
    invoice_notes='aliquid',
    invoice_status=shared.InvoiceStatusBulkInvoiceItemCreate.APPROVED,
    labels={
        "sint": 'officia',
    },
    line_item_description='dolor',
    line_item_detail='debitis',
    member_client_id='a',
    paid_date='dolorum',
    project_name='in',
    reimbursable_expense='illum',
    send_date='maiores',
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


res = s.bulk_invoice_batch_item.get(batch_id='rerum', batch_item_id='dicta')

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


res = s.bulk_invoice_batch_item.update(batch_id='magnam', batch_item_id='cumque', bulk_invoice_item_update=shared.BulkInvoiceItemUpdate(
    accepted_payment_methods=[
        shared.BulkInvoiceItemUpdateAcceptedPaymentMethods.LESS_THAN_NIL_GREATER_THAN_,
    ],
    amount=4118.2,
    bulk_invoice_batch_id='aliquid',
    bulk_invoice_item_merge_key='laborum',
    bulk_invoice_item_reference='accusamus',
    client_email='non',
    client_external_id='occaecati',
    credit_fee_handling='accusamus',
    due_date='delectus',
    invoice_notes='quidem',
    invoice_status=shared.InvoiceStatusBulkInvoiceItemUpdate.PAID,
    labels={
        "id": 'blanditiis',
    },
    line_item_description='deleniti',
    line_item_detail='sapiente',
    member_client_id='amet',
    paid_date='deserunt',
    project_name='nisi',
    reimbursable_expense='natus',
    send_date='omnis',
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


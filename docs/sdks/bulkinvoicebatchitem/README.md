# bulk_invoice_batch_item

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


res = s.bulk_invoice_batch_item.create(batch_id='distinctio', bulk_invoice_item_create=shared.BulkInvoiceItemCreate(
    accepted_payment_methods=[
        shared.BulkInvoiceItemCreateAcceptedPaymentMethods.ACH,
        shared.BulkInvoiceItemCreateAcceptedPaymentMethods.ACH,
        shared.BulkInvoiceItemCreateAcceptedPaymentMethods.ACH,
    ],
    amount=6180.16,
    bulk_invoice_batch_id='nobis',
    bulk_invoice_item_merge_key='eum',
    bulk_invoice_item_reference='vero',
    client_email='aspernatur',
    client_external_id='architecto',
    credit_fee_handling='et',
    due_date='excepturi',
    invoice_notes='ullam',
    invoice_status=shared.InvoiceStatusBulkInvoiceItemCreate.APPROVED,
    labels={
        "accusantium": 'mollitia',
        "reiciendis": 'mollitia',
        "ad": 'eum',
    },
    line_item_description='dolor',
    line_item_detail='necessitatibus',
    member_client_id='odit',
    paid_date='nemo',
    project_name='quasi',
    reimbursable_expense='doloribus',
    send_date='debitis',
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


res = s.bulk_invoice_batch_item.get(batch_id='eius', batch_item_id='maxime')

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


res = s.bulk_invoice_batch_item.update(batch_id='deleniti', batch_item_id='facilis', bulk_invoice_item_update=shared.BulkInvoiceItemUpdate(
    accepted_payment_methods=[
        shared.BulkInvoiceItemUpdateAcceptedPaymentMethods.CREDIT,
        shared.BulkInvoiceItemUpdateAcceptedPaymentMethods.CREDIT,
    ],
    amount=9194.83,
    bulk_invoice_batch_id='ullam',
    bulk_invoice_item_merge_key='expedita',
    bulk_invoice_item_reference='nihil',
    client_email='repellat',
    client_external_id='quibusdam',
    credit_fee_handling='saepe',
    due_date='pariatur',
    invoice_notes='accusantium',
    invoice_status=shared.InvoiceStatusBulkInvoiceItemUpdate.DRAFT,
    labels={
        "magni": 'sunt',
        "quo": 'illum',
        "pariatur": 'maxime',
    },
    line_item_description='ea',
    line_item_detail='excepturi',
    member_client_id='odit',
    paid_date='ea',
    project_name='accusantium',
    reimbursable_expense='maiores',
    send_date='quidem',
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


# BulkInvoiceItemCreate


## Fields

| Field                                                                                                                   | Type                                                                                                                    | Required                                                                                                                | Description                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `accepted_payment_methods`                                                                                              | list[[BulkInvoiceItemCreateAcceptedPaymentMethods](../../models/shared/bulkinvoiceitemcreateacceptedpaymentmethods.md)] | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `amount`                                                                                                                | *float*                                                                                                                 | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `bulk_invoice_batch_id`                                                                                                 | *str*                                                                                                                   | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `bulk_invoice_item_merge_key`                                                                                           | *Optional[str]*                                                                                                         | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `bulk_invoice_item_reference`                                                                                           | *Optional[str]*                                                                                                         | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `client_email`                                                                                                          | *Optional[str]*                                                                                                         | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `client_external_id`                                                                                                    | *Optional[str]*                                                                                                         | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `credit_fee_handling`                                                                                                   | *Optional[Any]*                                                                                                         | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `due_date`                                                                                                              | *str*                                                                                                                   | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `invoice_notes`                                                                                                         | *Optional[str]*                                                                                                         | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `invoice_status`                                                                                                        | [InvoiceStatusBulkInvoiceItemCreate](../../models/shared/invoicestatusbulkinvoiceitemcreate.md)                         | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `labels`                                                                                                                | *Optional[Any]*                                                                                                         | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `line_item_description`                                                                                                 | *str*                                                                                                                   | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `line_item_detail`                                                                                                      | *Optional[str]*                                                                                                         | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `member_client_id`                                                                                                      | *Optional[str]*                                                                                                         | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `paid_date`                                                                                                             | *Optional[str]*                                                                                                         | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `project_name`                                                                                                          | *Optional[str]*                                                                                                         | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `reimbursable_expense`                                                                                                  | *Optional[Any]*                                                                                                         | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
| `send_date`                                                                                                             | *Optional[str]*                                                                                                         | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |
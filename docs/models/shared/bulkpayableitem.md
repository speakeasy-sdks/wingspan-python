# BulkPayableItem

An item that will be converted into a payable


## Fields

| Field                                                                                                 | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `amount`                                                                                              | *float*                                                                                               | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `attachment_id`                                                                                       | *Optional[str]*                                                                                       | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `bulk_payable_batch_id`                                                                               | *str*                                                                                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `bulk_payable_item_id`                                                                                | *str*                                                                                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `bulk_payable_item_merge_key`                                                                         | *Optional[str]*                                                                                       | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `bulk_payable_item_reference`                                                                         | *Optional[str]*                                                                                       | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `client_id`                                                                                           | *str*                                                                                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `collaborator_email`                                                                                  | *Optional[str]*                                                                                       | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `collaborator_external_id`                                                                            | *Optional[str]*                                                                                       | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `collaborator_id`                                                                                     | *Optional[str]*                                                                                       | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `created_at`                                                                                          | *str*                                                                                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `due_date`                                                                                            | *str*                                                                                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `integration`                                                                                         | *Optional[Any]*                                                                                       | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `labels`                                                                                              | dict[str, *str*]                                                                                      | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `line_item_description`                                                                               | *str*                                                                                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `line_item_detail`                                                                                    | *Optional[str]*                                                                                       | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `metadata`                                                                                            | *Optional[Any]*                                                                                       | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `paid_date`                                                                                           | *str*                                                                                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `payable_notes`                                                                                       | *Optional[str]*                                                                                       | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `payable_status`                                                                                      | [PayableStatusBulkPayableItem](../../models/shared/payablestatusbulkpayableitem.md)                   | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `reimbursable_expense`                                                                                | *Optional[Any]*                                                                                       | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
| `status`                                                                                              | [StatusBulkPayableItem](../../models/shared/statusbulkpayableitem.md)                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `updated_at`                                                                                          | *str*                                                                                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `user_roles`                                                                                          | [UserRoles](../../models/shared/userroles.md)                                                         | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `workflow_sub_status`                                                                                 | [Optional[BulkPayableItemWorkflowSubStatus]](../../models/shared/bulkpayableitemworkflowsubstatus.md) | :heavy_minus_sign:                                                                                    | N/A                                                                                                   |
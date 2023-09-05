# InvoiceLineItem


## Fields

| Field                                         | Type                                          | Required                                      | Description                                   |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| `cost_per_unit`                               | *float*                                       | :heavy_check_mark:                            | N/A                                           |
| `created_at`                                  | *str*                                         | :heavy_check_mark:                            | N/A                                           |
| `description`                                 | *Optional[str]*                               | :heavy_minus_sign:                            | N/A                                           |
| `detail`                                      | *Optional[str]*                               | :heavy_minus_sign:                            | N/A                                           |
| `discount`                                    | *Optional[Any]*                               | :heavy_minus_sign:                            | N/A                                           |
| `integration`                                 | *Optional[Any]*                               | :heavy_minus_sign:                            | N/A                                           |
| `labels`                                      | dict[str, *str*]                              | :heavy_check_mark:                            | N/A                                           |
| `quantity`                                    | *float*                                       | :heavy_check_mark:                            | N/A                                           |
| `reimbursable_expense`                        | *bool*                                        | :heavy_check_mark:                            | N/A                                           |
| `total_cost`                                  | *float*                                       | :heavy_check_mark:                            | N/A                                           |
| `unit`                                        | *str*                                         | :heavy_check_mark:                            | N/A                                           |
| `updated_at`                                  | *str*                                         | :heavy_check_mark:                            | N/A                                           |
| `user_roles`                                  | [UserRoles](../../models/shared/userroles.md) | :heavy_check_mark:                            | N/A                                           |
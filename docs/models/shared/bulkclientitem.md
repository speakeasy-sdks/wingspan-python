# BulkClientItem

An item that will be converted into a client


## Fields

| Field                                                                           | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `bulk_client_batch_id`                                                          | *str*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `bulk_client_item_id`                                                           | *str*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `client_status`                                                                 | [ClientStatusBulkClientItem](../../models/shared/clientstatusbulkclientitem.md) | :heavy_check_mark:                                                              | N/A                                                                             |
| `company`                                                                       | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | N/A                                                                             |
| `created_at`                                                                    | *str*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `email`                                                                         | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | N/A                                                                             |
| `external_id`                                                                   | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | N/A                                                                             |
| `first_last_name`                                                               | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | N/A                                                                             |
| `integration`                                                                   | *Optional[Any]*                                                                 | :heavy_minus_sign:                                                              | N/A                                                                             |
| `labels`                                                                        | dict[str, *str*]                                                                | :heavy_check_mark:                                                              | N/A                                                                             |
| `member_client_id`                                                              | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | N/A                                                                             |
| `member_data`                                                                   | *Optional[Any]*                                                                 | :heavy_minus_sign:                                                              | N/A                                                                             |
| `member_id`                                                                     | *str*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `metadata`                                                                      | *Optional[Any]*                                                                 | :heavy_minus_sign:                                                              | N/A                                                                             |
| `status`                                                                        | [StatusBulkClientItem](../../models/shared/statusbulkclientitem.md)             | :heavy_check_mark:                                                              | N/A                                                                             |
| `updated_at`                                                                    | *str*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `user_roles`                                                                    | [UserRoles](../../models/shared/userroles.md)                                   | :heavy_check_mark:                                                              | N/A                                                                             |
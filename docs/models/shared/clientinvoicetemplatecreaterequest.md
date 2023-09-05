# ClientInvoiceTemplateCreateRequest


## Fields

| Field                                                                                                       | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                | *Optional[str]*                                                                                             | :heavy_minus_sign:                                                                                          | N/A                                                                                                         |
| `client_company`                                                                                            | *Optional[str]*                                                                                             | :heavy_minus_sign:                                                                                          | N/A                                                                                                         |
| `client_email`                                                                                              | *str*                                                                                                       | :heavy_check_mark:                                                                                          | N/A                                                                                                         |
| `client_email_cc`                                                                                           | list[*str*]                                                                                                 | :heavy_minus_sign:                                                                                          | N/A                                                                                                         |
| `client_first_name`                                                                                         | *Optional[str]*                                                                                             | :heavy_minus_sign:                                                                                          | N/A                                                                                                         |
| `client_last_name`                                                                                          | *Optional[str]*                                                                                             | :heavy_minus_sign:                                                                                          | N/A                                                                                                         |
| `due_in_days`                                                                                               | *Optional[float]*                                                                                           | :heavy_minus_sign:                                                                                          | N/A                                                                                                         |
| `frequency`                                                                                                 | *Optional[Any]*                                                                                             | :heavy_minus_sign:                                                                                          | N/A                                                                                                         |
| `invoice_data`                                                                                              | [ClientInvoiceDataCreateRequest](../../models/shared/clientinvoicedatacreaterequest.md)                     | :heavy_check_mark:                                                                                          | N/A                                                                                                         |
| `member_id`                                                                                                 | *str*                                                                                                       | :heavy_check_mark:                                                                                          | N/A                                                                                                         |
| `payment_method_id`                                                                                         | *Optional[str]*                                                                                             | :heavy_minus_sign:                                                                                          | N/A                                                                                                         |
| `schedule_dates`                                                                                            | list[*Any*]                                                                                                 | :heavy_minus_sign:                                                                                          | N/A                                                                                                         |
| `status`                                                                                                    | [StatusClientInvoiceTemplateCreateRequest](../../models/shared/statusclientinvoicetemplatecreaterequest.md) | :heavy_check_mark:                                                                                          | N/A                                                                                                         |
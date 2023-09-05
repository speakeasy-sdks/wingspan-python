# PayableSchema

A payable


## Fields

| Field                                                                                                                                                           | Type                                                                                                                                                            | Required                                                                                                                                                        | Description                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `accepted_payment_methods`                                                                                                                                      | list[[PayableSchemaAcceptedPaymentMethods](../../models/shared/payableschemaacceptedpaymentmethods.md)]                                                         | :heavy_minus_sign:                                                                                                                                              | N/A                                                                                                                                                             |
| `account_id`                                                                                                                                                    | *Optional[str]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                              | N/A                                                                                                                                                             |
| `amount`                                                                                                                                                        | *float*                                                                                                                                                         | :heavy_check_mark:                                                                                                                                              | N/A                                                                                                                                                             |
| `attachments`                                                                                                                                                   | [InvoiceAttachments](../../models/shared/invoiceattachments.md)                                                                                                 | :heavy_check_mark:                                                                                                                                              | N/A                                                                                                                                                             |
| `bank_transfer_info`                                                                                                                                            | *Optional[Any]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                              | N/A                                                                                                                                                             |
| `charged_fees`                                                                                                                                                  | *Optional[Any]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                              | N/A                                                                                                                                                             |
| `client`                                                                                                                                                        | [ClientOptions](../../models/shared/clientoptions.md)                                                                                                           | :heavy_check_mark:                                                                                                                                              | N/A                                                                                                                                                             |
| `client_id`                                                                                                                                                     | *str*                                                                                                                                                           | :heavy_check_mark:                                                                                                                                              | N/A                                                                                                                                                             |
| `collaborator_id`                                                                                                                                               | *str*                                                                                                                                                           | :heavy_check_mark:                                                                                                                                              | N/A                                                                                                                                                             |
| `created_at`                                                                                                                                                    | *str*                                                                                                                                                           | :heavy_check_mark:                                                                                                                                              | N/A                                                                                                                                                             |
| `credit_fee_handling`                                                                                                                                           | [FeeHandlingConfig](../../models/shared/feehandlingconfig.md)                                                                                                   | :heavy_check_mark:                                                                                                                                              | N/A                                                                                                                                                             |
| `currency`                                                                                                                                                      | [CurrencyPayableSchema](../../models/shared/currencypayableschema.md)                                                                                           | :heavy_check_mark:                                                                                                                                              | N/A                                                                                                                                                             |
| `due_date`                                                                                                                                                      | *str*                                                                                                                                                           | :heavy_check_mark:                                                                                                                                              | N/A                                                                                                                                                             |
| `events`                                                                                                                                                        | [InvoiceEvents](../../models/shared/invoiceevents.md)                                                                                                           | :heavy_check_mark:                                                                                                                                              | N/A                                                                                                                                                             |
| `integration`                                                                                                                                                   | [Sixb94b58d661f3eabc1444a7a43ac4b99580f0d050123b7bf38184e2f0d7bd66e](../../models/shared/sixb94b58d661f3eabc1444a7a43ac4b99580f0d050123b7bf38184e2f0d7bd66e.md) | :heavy_check_mark:                                                                                                                                              | N/A                                                                                                                                                             |
| `international_bank_transfer_info`                                                                                                                              | *Optional[Any]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                              | N/A                                                                                                                                                             |
| `invoice_notes`                                                                                                                                                 | *str*                                                                                                                                                           | :heavy_check_mark:                                                                                                                                              | N/A                                                                                                                                                             |
| `invoice_number`                                                                                                                                                | *str*                                                                                                                                                           | :heavy_check_mark:                                                                                                                                              | N/A                                                                                                                                                             |
| `invoice_template_id`                                                                                                                                           | *str*                                                                                                                                                           | :heavy_check_mark:                                                                                                                                              | N/A                                                                                                                                                             |
| `labels`                                                                                                                                                        | dict[str, *str*]                                                                                                                                                | :heavy_check_mark:                                                                                                                                              | N/A                                                                                                                                                             |
| `late_fee_handling`                                                                                                                                             | [LateFeeConfig](../../models/shared/latefeeconfig.md)                                                                                                           | :heavy_check_mark:                                                                                                                                              | N/A                                                                                                                                                             |
| `line_items`                                                                                                                                                    | list[[InvoiceLineItem](../../models/shared/invoicelineitem.md)]                                                                                                 | :heavy_check_mark:                                                                                                                                              | N/A                                                                                                                                                             |
| `member`                                                                                                                                                        | [MemberOptions](../../models/shared/memberoptions.md)                                                                                                           | :heavy_check_mark:                                                                                                                                              | N/A                                                                                                                                                             |
| `member_address`                                                                                                                                                | [Address](../../models/shared/address.md)                                                                                                                       | :heavy_check_mark:                                                                                                                                              | N/A                                                                                                                                                             |
| `member_formatted_address_lines`                                                                                                                                | list[*str*]                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                              | N/A                                                                                                                                                             |
| `member_id`                                                                                                                                                     | *str*                                                                                                                                                           | :heavy_check_mark:                                                                                                                                              | N/A                                                                                                                                                             |
| `metadata`                                                                                                                                                      | *Optional[Any]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                              | N/A                                                                                                                                                             |
| `next_payroll_execution_date`                                                                                                                                   | *Optional[Any]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                              | N/A                                                                                                                                                             |
| `notification_preferences`                                                                                                                                      | [InvoiceNotificationPreferences](../../models/shared/invoicenotificationpreferences.md)                                                                         | :heavy_check_mark:                                                                                                                                              | N/A                                                                                                                                                             |
| `payable_id`                                                                                                                                                    | *str*                                                                                                                                                           | :heavy_check_mark:                                                                                                                                              | N/A                                                                                                                                                             |
| `payment_method_id`                                                                                                                                             | *Optional[str]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                              | N/A                                                                                                                                                             |
| `source_id`                                                                                                                                                     | *Optional[str]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                              | N/A                                                                                                                                                             |
| `status`                                                                                                                                                        | [StatusPayableSchema](../../models/shared/statuspayableschema.md)                                                                                               | :heavy_check_mark:                                                                                                                                              | N/A                                                                                                                                                             |
| `updated_at`                                                                                                                                                    | *str*                                                                                                                                                           | :heavy_check_mark:                                                                                                                                              | N/A                                                                                                                                                             |
| `user_roles`                                                                                                                                                    | [UserRoles](../../models/shared/userroles.md)                                                                                                                   | :heavy_check_mark:                                                                                                                                              | N/A                                                                                                                                                             |
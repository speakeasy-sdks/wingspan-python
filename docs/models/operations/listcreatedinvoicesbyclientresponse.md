# ListCreatedInvoicesByClientResponse


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `client_invoices`                                                                     | list[[shared.ClientInvoice](../../models/shared/clientinvoice.md)]                    | :heavy_minus_sign:                                                                    | A list of Client Created Invoices                                                     |
| `content_type`                                                                        | *str*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `status_code`                                                                         | *int*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `raw_response`                                                                        | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response) | :heavy_minus_sign:                                                                    | N/A                                                                                   |
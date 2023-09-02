# Wingspan SDK

## Overview

Wingspan Payments API: Payments

### Available Operations

* [delete_payments_banking_card_id_](#delete_payments_banking_card_id_) - delete a card by cardId
* [delete_payments_banking_instant_payout](#delete_payments_banking_instant_payout) - delete instant payout
* [delete_payments_collaborator_settings_additional_data_id_](#delete_payments_collaborator_settings_additional_data_id_) - Delete additional data
* [delete_payments_collaborator_settings_eligibility_requirement_id_](#delete_payments_collaborator_settings_eligibility_requirement_id_) - Delete Eligibility Requirement
* [delete_payments_collaborator_settings_payment_eligibility_id_](#delete_payments_collaborator_settings_payment_eligibility_id_) - Delete Payment Eligibility Requirement
* [delete_payments_payout_settings_member_id_debit_card_id_](#delete_payments_payout_settings_member_id_debit_card_id_) - delete the payout debit card
* [get_payments](#get_payments) - getServiceStatus
* [get_payments_banking_card](#get_payments_banking_card) - list cards
* [get_payments_banking_instant_payout](#get_payments_banking_instant_payout) - fetch instant payout details
* [get_payments_banking_institution_routing_number_](#get_payments_banking_institution_routing_number_) - Get Institution By Routing Number
* [get_payments_banking_statement](#get_payments_banking_statement) - list bank statements
* [get_payments_banking_statement_id_](#get_payments_banking_statement_id_) - get bank statement
* [get_payments_banking_statement_id_download](#get_payments_banking_statement_id_download) - download bank statement pdf
* [get_payments_bulk_payable_batch_batch_id_import_summary](#get_payments_bulk_payable_batch_batch_id_import_summary) - Get Bulk Payable Batch Import Summary
* [get_payments_client_invoice_invoice_id_fees](#get_payments_client_invoice_invoice_id_fees) - list client-invoice fees
* [get_payments_collaborator_settings_additional_data](#get_payments_collaborator_settings_additional_data) - list additional settings
* [get_payments_collaborator_settings_additional_data_id_](#get_payments_collaborator_settings_additional_data_id_) - Get additional data
* [get_payments_collaborator_settings_eligibility_requirement](#get_payments_collaborator_settings_eligibility_requirement) - List Eligibility Requirements
* [get_payments_collaborator_settings_eligibility_requirement_id_](#get_payments_collaborator_settings_eligibility_requirement_id_) - Get Eligibility Requirement
* [get_payments_collaborator_settings_payment_eligibility](#get_payments_collaborator_settings_payment_eligibility) - List Payment Eligigbility Requirements
* [get_payments_collaborator_settings_payment_eligibility_id_](#get_payments_collaborator_settings_payment_eligibility_id_) - Get Payment Eligibility Requirement
* [get_payments_collaborator_id_download_1099_year_index_](#get_payments_collaborator_id_download_1099_year_index_) - Downloads a form 1099 PDF for a collaborator
* [get_payments_collaborator_id_download_w9](#get_payments_collaborator_id_download_w9) - Downloads a form W9 PDF for a collaborator
* [get_payments_collaborator_id_events](#get_payments_collaborator_id_events) - Get collaborator events by collaboratorId
* [get_payments_mcc](#get_payments_mcc) - list mcc codes
* [get_payments_payout_settings_id_](#get_payments_payout_settings_id_) - get the payout settings
* [get_payments_payout_settings_member_id_debit_card](#get_payments_payout_settings_member_id_debit_card) - list the payout debit cards
* [get_payments_payout_settings_member_id_debit_card_id_](#get_payments_payout_settings_member_id_debit_card_id_) - get the payout debit card
* [get_payments_service_banking_member_id_application](#get_payments_service_banking_member_id_application) - gets an application link for creating the clearing bank account
* [get_payments_summary_payables](#get_payments_summary_payables) - get payables summary
* [patch_payments_banking_card_id_](#patch_payments_banking_card_id_) - update card by cardId
* [patch_payments_banking_card_id_token](#patch_payments_banking_card_id_token) - exchange the code for a token
* [patch_payments_collaborator_settings_eligibility_requirement_id_](#patch_payments_collaborator_settings_eligibility_requirement_id_) - Update Eligibility Requirement
* [post_payments_banking_card_id_token](#post_payments_banking_card_id_token) - sends a verification code
* [post_payments_banking_instant_payout](#post_payments_banking_instant_payout) - create instant payout details
* [post_payments_collaborator_settings_additional_data](#post_payments_collaborator_settings_additional_data) - Create additional data
* [post_payments_collaborator_settings_eligibility_requirement](#post_payments_collaborator_settings_eligibility_requirement) - Create Eligibility Requirement
* [post_payments_collaborator_settings_payment_eligibility](#post_payments_collaborator_settings_payment_eligibility) - Create Payment Eligibility Requirement
* [post_payments_collaborator_1099_mark_undelivered](#post_payments_collaborator_1099_mark_undelivered) - Mark a 1099 submission as returned by mail for collaborator
* [post_payments_collaborator_1099_remail](#post_payments_collaborator_1099_remail) - Re-mail 1099 submission for collaborator

## delete_payments_banking_card_id_

delete a card by cardId

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()

req = operations.DeletePaymentsBankingCardIDRequest(
    id='a05dfc2d-df7c-4c78-8a1b-a928fc816742',
)

res = s.wingspan.delete_payments_banking_card_id_(req)

if res.card is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.DeletePaymentsBankingCardIDRequest](../../models/operations/deletepaymentsbankingcardidrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.DeletePaymentsBankingCardIDResponse](../../models/operations/deletepaymentsbankingcardidresponse.md)**


## delete_payments_banking_instant_payout

delete instant payout

### Example Usage

```python
import wingspan


s = wingspan.Wingspan()


res = s.wingspan.delete_payments_banking_instant_payout()

if res.instant_payout_response is not None:
    # handle response
```


### Response

**[operations.DeletePaymentsBankingInstantPayoutResponse](../../models/operations/deletepaymentsbankinginstantpayoutresponse.md)**


## delete_payments_collaborator_settings_additional_data_id_

Delete additional data

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()

req = operations.DeletePaymentsCollaboratorSettingsAdditionalDataIDRequest(
    id='cb739205-9293-496f-aa75-96eb10faaa23',
)

res = s.wingspan.delete_payments_collaborator_settings_additional_data_id_(req)

if res.additional_data is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                    | Type                                                                                                                                                         | Required                                                                                                                                                     | Description                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                    | [operations.DeletePaymentsCollaboratorSettingsAdditionalDataIDRequest](../../models/operations/deletepaymentscollaboratorsettingsadditionaldataidrequest.md) | :heavy_check_mark:                                                                                                                                           | The request object to use for the request.                                                                                                                   |


### Response

**[operations.DeletePaymentsCollaboratorSettingsAdditionalDataIDResponse](../../models/operations/deletepaymentscollaboratorsettingsadditionaldataidresponse.md)**


## delete_payments_collaborator_settings_eligibility_requirement_id_

Delete Eligibility Requirement

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()

req = operations.DeletePaymentsCollaboratorSettingsEligibilityRequirementIDRequest(
    id='52c59559-07af-4f1a-ba2f-a9467739251a',
)

res = s.wingspan.delete_payments_collaborator_settings_eligibility_requirement_id_(req)

if res.eligibility_requirements is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                    | [operations.DeletePaymentsCollaboratorSettingsEligibilityRequirementIDRequest](../../models/operations/deletepaymentscollaboratorsettingseligibilityrequirementidrequest.md) | :heavy_check_mark:                                                                                                                                                           | The request object to use for the request.                                                                                                                                   |


### Response

**[operations.DeletePaymentsCollaboratorSettingsEligibilityRequirementIDResponse](../../models/operations/deletepaymentscollaboratorsettingseligibilityrequirementidresponse.md)**


## delete_payments_collaborator_settings_payment_eligibility_id_

Delete Payment Eligibility Requirement

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()

req = operations.DeletePaymentsCollaboratorSettingsPaymentEligibilityIDRequest(
    id='a52c3f5a-d019-4da1-bfe7-8f097b0074f1',
)

res = s.wingspan.delete_payments_collaborator_settings_payment_eligibility_id_(req)

if res.payment_eligibility is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                            | Type                                                                                                                                                                 | Required                                                                                                                                                             | Description                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                            | [operations.DeletePaymentsCollaboratorSettingsPaymentEligibilityIDRequest](../../models/operations/deletepaymentscollaboratorsettingspaymenteligibilityidrequest.md) | :heavy_check_mark:                                                                                                                                                   | The request object to use for the request.                                                                                                                           |


### Response

**[operations.DeletePaymentsCollaboratorSettingsPaymentEligibilityIDResponse](../../models/operations/deletepaymentscollaboratorsettingspaymenteligibilityidresponse.md)**


## delete_payments_payout_settings_member_id_debit_card_id_

delete the payout debit card

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()

req = operations.DeletePaymentsPayoutSettingsMemberIDDebitCardIDRequest(
    id='5471b5e6-e13b-499d-888e-1e91e450ad2a',
    member_id='distinctio',
)

res = s.wingspan.delete_payments_payout_settings_member_id_debit_card_id_(req)

if res.checkbook_card is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                              | Type                                                                                                                                                   | Required                                                                                                                                               | Description                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                              | [operations.DeletePaymentsPayoutSettingsMemberIDDebitCardIDRequest](../../models/operations/deletepaymentspayoutsettingsmemberiddebitcardidrequest.md) | :heavy_check_mark:                                                                                                                                     | The request object to use for the request.                                                                                                             |


### Response

**[operations.DeletePaymentsPayoutSettingsMemberIDDebitCardIDResponse](../../models/operations/deletepaymentspayoutsettingsmemberiddebitcardidresponse.md)**


## get_payments

getServiceStatus

### Example Usage

```python
import wingspan


s = wingspan.Wingspan()


res = s.wingspan.get_payments()

if res.ping is not None:
    # handle response
```


### Response

**[operations.GetPaymentsResponse](../../models/operations/getpaymentsresponse.md)**


## get_payments_banking_card

list cards

### Example Usage

```python
import wingspan


s = wingspan.Wingspan()


res = s.wingspan.get_payments_banking_card()

if res.cards is not None:
    # handle response
```


### Response

**[operations.GetPaymentsBankingCardResponse](../../models/operations/getpaymentsbankingcardresponse.md)**


## get_payments_banking_instant_payout

fetch instant payout details

### Example Usage

```python
import wingspan


s = wingspan.Wingspan()


res = s.wingspan.get_payments_banking_instant_payout()

if res.instant_payout_response is not None:
    # handle response
```


### Response

**[operations.GetPaymentsBankingInstantPayoutResponse](../../models/operations/getpaymentsbankinginstantpayoutresponse.md)**


## get_payments_banking_institution_routing_number_

Get Institution By Routing Number

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()

req = operations.GetPaymentsBankingInstitutionRoutingNumberRequest(
    routing_number='quibusdam',
)

res = s.wingspan.get_payments_banking_institution_routing_number_(req)

if res.institution_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                    | [operations.GetPaymentsBankingInstitutionRoutingNumberRequest](../../models/operations/getpaymentsbankinginstitutionroutingnumberrequest.md) | :heavy_check_mark:                                                                                                                           | The request object to use for the request.                                                                                                   |


### Response

**[operations.GetPaymentsBankingInstitutionRoutingNumberResponse](../../models/operations/getpaymentsbankinginstitutionroutingnumberresponse.md)**


## get_payments_banking_statement

list bank statements

### Example Usage

```python
import wingspan


s = wingspan.Wingspan()


res = s.wingspan.get_payments_banking_statement()

if res.bank_statements is not None:
    # handle response
```


### Response

**[operations.GetPaymentsBankingStatementResponse](../../models/operations/getpaymentsbankingstatementresponse.md)**


## get_payments_banking_statement_id_

get bank statement

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()

req = operations.GetPaymentsBankingStatementIDRequest(
    id='44269802-d502-4a94-bb4f-63c969e9a3ef',
)

res = s.wingspan.get_payments_banking_statement_id_(req)

if res.bank_statements is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.GetPaymentsBankingStatementIDRequest](../../models/operations/getpaymentsbankingstatementidrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.GetPaymentsBankingStatementIDResponse](../../models/operations/getpaymentsbankingstatementidresponse.md)**


## get_payments_banking_statement_id_download

download bank statement pdf

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()

req = operations.GetPaymentsBankingStatementIDDownloadRequest(
    id='a77dfb14-cd66-4ae3-95ef-b9ba88f3a669',
)

res = s.wingspan.get_payments_banking_statement_id_download(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                          | [operations.GetPaymentsBankingStatementIDDownloadRequest](../../models/operations/getpaymentsbankingstatementiddownloadrequest.md) | :heavy_check_mark:                                                                                                                 | The request object to use for the request.                                                                                         |


### Response

**[operations.GetPaymentsBankingStatementIDDownloadResponse](../../models/operations/getpaymentsbankingstatementiddownloadresponse.md)**


## get_payments_bulk_payable_batch_batch_id_import_summary

Get Bulk Payable Batch Import Summary

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()

req = operations.GetPaymentsBulkPayableBatchBatchIDImportSummaryRequest(
    batch_id='omnis',
)

res = s.wingspan.get_payments_bulk_payable_batch_batch_id_import_summary(req)

if res.bulk_payable_import_summary is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                              | Type                                                                                                                                                   | Required                                                                                                                                               | Description                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                              | [operations.GetPaymentsBulkPayableBatchBatchIDImportSummaryRequest](../../models/operations/getpaymentsbulkpayablebatchbatchidimportsummaryrequest.md) | :heavy_check_mark:                                                                                                                                     | The request object to use for the request.                                                                                                             |


### Response

**[operations.GetPaymentsBulkPayableBatchBatchIDImportSummaryResponse](../../models/operations/getpaymentsbulkpayablebatchbatchidimportsummaryresponse.md)**


## get_payments_client_invoice_invoice_id_fees

list client-invoice fees

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()

req = operations.GetPaymentsClientInvoiceInvoiceIDFeesRequest(
    invoice_id='molestiae',
)

res = s.wingspan.get_payments_client_invoice_invoice_id_fees(req)

if res.invoice_fee_calculation is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                          | [operations.GetPaymentsClientInvoiceInvoiceIDFeesRequest](../../models/operations/getpaymentsclientinvoiceinvoiceidfeesrequest.md) | :heavy_check_mark:                                                                                                                 | The request object to use for the request.                                                                                         |


### Response

**[operations.GetPaymentsClientInvoiceInvoiceIDFeesResponse](../../models/operations/getpaymentsclientinvoiceinvoiceidfeesresponse.md)**


## get_payments_collaborator_settings_additional_data

list additional settings

### Example Usage

```python
import wingspan


s = wingspan.Wingspan()


res = s.wingspan.get_payments_collaborator_settings_additional_data()

if res.additional_data is not None:
    # handle response
```


### Response

**[operations.GetPaymentsCollaboratorSettingsAdditionalDataResponse](../../models/operations/getpaymentscollaboratorsettingsadditionaldataresponse.md)**


## get_payments_collaborator_settings_additional_data_id_

Get additional data

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()

req = operations.GetPaymentsCollaboratorSettingsAdditionalDataIDRequest(
    id='074ba446-9b6e-4214-9959-890afa563e25',
)

res = s.wingspan.get_payments_collaborator_settings_additional_data_id_(req)

if res.additional_data is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                              | Type                                                                                                                                                   | Required                                                                                                                                               | Description                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                              | [operations.GetPaymentsCollaboratorSettingsAdditionalDataIDRequest](../../models/operations/getpaymentscollaboratorsettingsadditionaldataidrequest.md) | :heavy_check_mark:                                                                                                                                     | The request object to use for the request.                                                                                                             |


### Response

**[operations.GetPaymentsCollaboratorSettingsAdditionalDataIDResponse](../../models/operations/getpaymentscollaboratorsettingsadditionaldataidresponse.md)**


## get_payments_collaborator_settings_eligibility_requirement

List Eligibility Requirements

### Example Usage

```python
import wingspan


s = wingspan.Wingspan()


res = s.wingspan.get_payments_collaborator_settings_eligibility_requirement()

if res.eligibility_requirements is not None:
    # handle response
```


### Response

**[operations.GetPaymentsCollaboratorSettingsEligibilityRequirementResponse](../../models/operations/getpaymentscollaboratorsettingseligibilityrequirementresponse.md)**


## get_payments_collaborator_settings_eligibility_requirement_id_

Get Eligibility Requirement

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()

req = operations.GetPaymentsCollaboratorSettingsEligibilityRequirementIDRequest(
    id='16fe4c8b-711e-45b7-bd2e-d028921cddc6',
)

res = s.wingspan.get_payments_collaborator_settings_eligibility_requirement_id_(req)

if res.eligibility_requirements is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                              | Type                                                                                                                                                                   | Required                                                                                                                                                               | Description                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                              | [operations.GetPaymentsCollaboratorSettingsEligibilityRequirementIDRequest](../../models/operations/getpaymentscollaboratorsettingseligibilityrequirementidrequest.md) | :heavy_check_mark:                                                                                                                                                     | The request object to use for the request.                                                                                                                             |


### Response

**[operations.GetPaymentsCollaboratorSettingsEligibilityRequirementIDResponse](../../models/operations/getpaymentscollaboratorsettingseligibilityrequirementidresponse.md)**


## get_payments_collaborator_settings_payment_eligibility

List Payment Eligigbility Requirements

### Example Usage

```python
import wingspan


s = wingspan.Wingspan()


res = s.wingspan.get_payments_collaborator_settings_payment_eligibility()

if res.payment_eligibilities is not None:
    # handle response
```


### Response

**[operations.GetPaymentsCollaboratorSettingsPaymentEligibilityResponse](../../models/operations/getpaymentscollaboratorsettingspaymenteligibilityresponse.md)**


## get_payments_collaborator_settings_payment_eligibility_id_

Get Payment Eligibility Requirement

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()

req = operations.GetPaymentsCollaboratorSettingsPaymentEligibilityIDRequest(
    id='92601fb5-76b0-4d5f-8d30-c5fbb2587053',
)

res = s.wingspan.get_payments_collaborator_settings_payment_eligibility_id_(req)

if res.payment_eligibility is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                      | Type                                                                                                                                                           | Required                                                                                                                                                       | Description                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                      | [operations.GetPaymentsCollaboratorSettingsPaymentEligibilityIDRequest](../../models/operations/getpaymentscollaboratorsettingspaymenteligibilityidrequest.md) | :heavy_check_mark:                                                                                                                                             | The request object to use for the request.                                                                                                                     |


### Response

**[operations.GetPaymentsCollaboratorSettingsPaymentEligibilityIDResponse](../../models/operations/getpaymentscollaboratorsettingspaymenteligibilityidresponse.md)**


## get_payments_collaborator_id_download_1099_year_index_

Downloads a form 1099 PDF for a collaborator

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()

req = operations.GetPaymentsCollaboratorIDDownload1099YearIndexRequest(
    id='202c73d5-fe9b-490c-a890-9b3fe49a8d9c',
    index='libero',
    year='delectus',
)

res = s.wingspan.get_payments_collaborator_id_download_1099_year_index_(req)

if res.download1099_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                            | Type                                                                                                                                                 | Required                                                                                                                                             | Description                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                            | [operations.GetPaymentsCollaboratorIDDownload1099YearIndexRequest](../../models/operations/getpaymentscollaboratoriddownload1099yearindexrequest.md) | :heavy_check_mark:                                                                                                                                   | The request object to use for the request.                                                                                                           |


### Response

**[operations.GetPaymentsCollaboratorIDDownload1099YearIndexResponse](../../models/operations/getpaymentscollaboratoriddownload1099yearindexresponse.md)**


## get_payments_collaborator_id_download_w9

Downloads a form W9 PDF for a collaborator

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()

req = operations.GetPaymentsCollaboratorIDDownloadW9Request(
    id='48633323-f9b7-47f3-a410-0674ebf69280',
)

res = s.wingspan.get_payments_collaborator_id_download_w9(req)

if res.download_w9_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.GetPaymentsCollaboratorIDDownloadW9Request](../../models/operations/getpaymentscollaboratoriddownloadw9request.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |


### Response

**[operations.GetPaymentsCollaboratorIDDownloadW9Response](../../models/operations/getpaymentscollaboratoriddownloadw9response.md)**


## get_payments_collaborator_id_events

Get collaborator events by collaboratorId

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()

req = operations.GetPaymentsCollaboratorIDEventsRequest(
    id='d1ba77a8-9ebf-4737-ae42-03ce5e6a95d8',
)

res = s.wingspan.get_payments_collaborator_id_events(req)

if res.collaborator_events is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.GetPaymentsCollaboratorIDEventsRequest](../../models/operations/getpaymentscollaboratorideventsrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.GetPaymentsCollaboratorIDEventsResponse](../../models/operations/getpaymentscollaboratorideventsresponse.md)**


## get_payments_mcc

list mcc codes

### Example Usage

```python
import wingspan


s = wingspan.Wingspan()


res = s.wingspan.get_payments_mcc()

if res.mcc_responses is not None:
    # handle response
```


### Response

**[operations.GetPaymentsMccResponse](../../models/operations/getpaymentsmccresponse.md)**


## get_payments_payout_settings_id_

get the payout settings

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()

req = operations.GetPaymentsPayoutSettingsIDRequest(
    id='a0d446ce-2af7-4a73-8f3b-e453f870b326',
)

res = s.wingspan.get_payments_payout_settings_id_(req)

if res.payout_settings_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.GetPaymentsPayoutSettingsIDRequest](../../models/operations/getpaymentspayoutsettingsidrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.GetPaymentsPayoutSettingsIDResponse](../../models/operations/getpaymentspayoutsettingsidresponse.md)**


## get_payments_payout_settings_member_id_debit_card

list the payout debit cards

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()

req = operations.GetPaymentsPayoutSettingsMemberIDDebitCardRequest(
    member_id='libero',
)

res = s.wingspan.get_payments_payout_settings_member_id_debit_card(req)

if res.checkbook_cards is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                    | [operations.GetPaymentsPayoutSettingsMemberIDDebitCardRequest](../../models/operations/getpaymentspayoutsettingsmemberiddebitcardrequest.md) | :heavy_check_mark:                                                                                                                           | The request object to use for the request.                                                                                                   |


### Response

**[operations.GetPaymentsPayoutSettingsMemberIDDebitCardResponse](../../models/operations/getpaymentspayoutsettingsmemberiddebitcardresponse.md)**


## get_payments_payout_settings_member_id_debit_card_id_

get the payout debit card

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()

req = operations.GetPaymentsPayoutSettingsMemberIDDebitCardIDRequest(
    id='5a73429c-db1a-4842-abb6-79d2322715bf',
    member_id='voluptatem',
)

res = s.wingspan.get_payments_payout_settings_member_id_debit_card_id_(req)

if res.checkbook_card is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                        | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                        | [operations.GetPaymentsPayoutSettingsMemberIDDebitCardIDRequest](../../models/operations/getpaymentspayoutsettingsmemberiddebitcardidrequest.md) | :heavy_check_mark:                                                                                                                               | The request object to use for the request.                                                                                                       |


### Response

**[operations.GetPaymentsPayoutSettingsMemberIDDebitCardIDResponse](../../models/operations/getpaymentspayoutsettingsmemberiddebitcardidresponse.md)**


## get_payments_service_banking_member_id_application

gets an application link for creating the clearing bank account

### Example Usage

```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()

req = operations.GetPaymentsServiceBankingMemberIDApplicationRequest(
    member_id='cumque',
)

res = s.wingspan.get_payments_service_banking_member_id_application(req)

if res.banking_application_form is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                        | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                        | [operations.GetPaymentsServiceBankingMemberIDApplicationRequest](../../models/operations/getpaymentsservicebankingmemberidapplicationrequest.md) | :heavy_check_mark:                                                                                                                               | The request object to use for the request.                                                                                                       |


### Response

**[operations.GetPaymentsServiceBankingMemberIDApplicationResponse](../../models/operations/getpaymentsservicebankingmemberidapplicationresponse.md)**


## get_payments_summary_payables

get payables summary

### Example Usage

```python
import wingspan


s = wingspan.Wingspan()


res = s.wingspan.get_payments_summary_payables()

if res.payables_summary is not None:
    # handle response
```


### Response

**[operations.GetPaymentsSummaryPayablesResponse](../../models/operations/getpaymentssummarypayablesresponse.md)**


## patch_payments_banking_card_id_

update card by cardId

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()

req = operations.PatchPaymentsBankingCardIDRequest(
    card_update_request=shared.CardUpdateRequest(
        status=shared.CardUpdateRequestStatus.FROZEN,
    ),
    id='b1e31b8b-90f3-4443-a110-8e0adcf4b921',
)

res = s.wingspan.patch_payments_banking_card_id_(req)

if res.card is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.PatchPaymentsBankingCardIDRequest](../../models/operations/patchpaymentsbankingcardidrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.PatchPaymentsBankingCardIDResponse](../../models/operations/patchpaymentsbankingcardidresponse.md)**


## patch_payments_banking_card_id_token

exchange the code for a token

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()

req = operations.PatchPaymentsBankingCardIDTokenRequest(
    card_token_request=shared.CardTokenRequest(
        verification_code='laudantium',
        verification_token='odio',
    ),
    id='9fce953f-73ef-47fb-87ab-d74dd39c0f5d',
)

res = s.wingspan.patch_payments_banking_card_id_token(req)

if res.card_token_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.PatchPaymentsBankingCardIDTokenRequest](../../models/operations/patchpaymentsbankingcardidtokenrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.PatchPaymentsBankingCardIDTokenResponse](../../models/operations/patchpaymentsbankingcardidtokenresponse.md)**


## patch_payments_collaborator_settings_eligibility_requirement_id_

Update Eligibility Requirement

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()

req = operations.PatchPaymentsCollaboratorSettingsEligibilityRequirementIDRequest(
    eligibility_requirement_update_request=shared.EligibilityRequirementUpdateRequest(
        requirement_type=shared.EligibilityRequirementUpdateRequestRequirementType.SIGNATURE,
        template_id='fugit',
        valid_for=7804.27,
    ),
    id='ff7c70a4-5626-4d43-a813-f16d9f5fce6c',
)

res = s.wingspan.patch_payments_collaborator_settings_eligibility_requirement_id_(req)

if res.eligibility_requirements is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                  | Type                                                                                                                                                                       | Required                                                                                                                                                                   | Description                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                  | [operations.PatchPaymentsCollaboratorSettingsEligibilityRequirementIDRequest](../../models/operations/patchpaymentscollaboratorsettingseligibilityrequirementidrequest.md) | :heavy_check_mark:                                                                                                                                                         | The request object to use for the request.                                                                                                                                 |


### Response

**[operations.PatchPaymentsCollaboratorSettingsEligibilityRequirementIDResponse](../../models/operations/patchpaymentscollaboratorsettingseligibilityrequirementidresponse.md)**


## post_payments_banking_card_id_token

sends a verification code

### Example Usage

```python
import wingspan
from wingspan.models import operations, shared

s = wingspan.Wingspan()

req = operations.PostPaymentsBankingCardIDTokenRequest(
    card_code_request=shared.CardCodeRequest(
        channel='corporis',
    ),
    id='56146c3e-250f-4b00-8c42-e141aac366c8',
)

res = s.wingspan.post_payments_banking_card_id_token(req)

if res.card_code_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.PostPaymentsBankingCardIDTokenRequest](../../models/operations/postpaymentsbankingcardidtokenrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.PostPaymentsBankingCardIDTokenResponse](../../models/operations/postpaymentsbankingcardidtokenresponse.md)**


## post_payments_banking_instant_payout

create instant payout details

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()

req = shared.InstantPayoutRequest(
    external_payout_account_token='assumenda',
)

res = s.wingspan.post_payments_banking_instant_payout(req)

if res.instant_payout_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [shared.InstantPayoutRequest](../../models/shared/instantpayoutrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.PostPaymentsBankingInstantPayoutResponse](../../models/operations/postpaymentsbankinginstantpayoutresponse.md)**


## post_payments_collaborator_settings_additional_data

Create additional data

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()

req = shared.AdditionalData(
    key='nulla',
    name='Jeannette Boyer',
    required=False,
    type=shared.AdditionalDataType.BOOLEAN,
)

res = s.wingspan.post_payments_collaborator_settings_additional_data(req)

if res.additional_data is not None:
    # handle response
```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `request`                                                      | [shared.AdditionalData](../../models/shared/additionaldata.md) | :heavy_check_mark:                                             | The request object to use for the request.                     |


### Response

**[operations.PostPaymentsCollaboratorSettingsAdditionalDataResponse](../../models/operations/postpaymentscollaboratorsettingsadditionaldataresponse.md)**


## post_payments_collaborator_settings_eligibility_requirement

Create Eligibility Requirement

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()

req = shared.EligibilityRequirementCreateRequest(
    requirement_type=shared.EligibilityRequirementCreateRequestRequirementType.SIGNATURE,
    template_id='provident',
    valid_for=553.74,
)

res = s.wingspan.post_payments_collaborator_settings_eligibility_requirement(req)

if res.eligibility_requirement is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [shared.EligibilityRequirementCreateRequest](../../models/shared/eligibilityrequirementcreaterequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.PostPaymentsCollaboratorSettingsEligibilityRequirementResponse](../../models/operations/postpaymentscollaboratorsettingseligibilityrequirementresponse.md)**


## post_payments_collaborator_settings_payment_eligibility

Create Payment Eligibility Requirement

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()

req = shared.PaymentEligibility(
    field='molestiae',
    value='magnam',
)

res = s.wingspan.post_payments_collaborator_settings_payment_eligibility(req)

if res.payment_eligibility is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [shared.PaymentEligibility](../../models/shared/paymenteligibility.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.PostPaymentsCollaboratorSettingsPaymentEligibilityResponse](../../models/operations/postpaymentscollaboratorsettingspaymenteligibilityresponse.md)**


## post_payments_collaborator_1099_mark_undelivered

Mark a 1099 submission as returned by mail for collaborator

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()

req = shared.Mark1099AsUndeliveredRequest(
    member_id='odio',
    submission_index=2621.18,
    year=4585.15,
)

res = s.wingspan.post_payments_collaborator_1099_mark_undelivered(req)

if res.mark1099_as_undelivered_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [shared.Mark1099AsUndeliveredRequest](../../models/shared/mark1099asundeliveredrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.PostPaymentsCollaborator1099MarkUndeliveredResponse](../../models/operations/postpaymentscollaborator1099markundeliveredresponse.md)**


## post_payments_collaborator_1099_remail

Re-mail 1099 submission for collaborator

### Example Usage

```python
import wingspan
from wingspan.models import shared

s = wingspan.Wingspan()

req = shared.Remail1099Request(
    address=shared.Sevenb49dbbd81f36ab6d7b4f07c5e2e53f40e36eb7b83d1488f379e993b830eec56(
        address_line1='esse',
        address_line2='rem',
        city='Kihnchester',
        postal_code='24381-5700',
        state='id',
    ),
    document_index=6969.97,
    member_id='neque',
    year=7786.96,
)

res = s.wingspan.post_payments_collaborator_1099_remail(req)

if res.remail1099_response is not None:
    # handle response
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [shared.Remail1099Request](../../models/shared/remail1099request.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.PostPaymentsCollaborator1099RemailResponse](../../models/operations/postpaymentscollaborator1099remailresponse.md)**


# Wingspan Python SDK

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/wingspan-python.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->


```python
import wingspan
from wingspan.models import operations

s = wingspan.Wingspan()

req = operations.DeletePaymentsBankingCardIDRequest(
    id='89bd9d8d-69a6-474e-8f46-7cc8796ed151',
)

res = s.delete_payments_banking_card_id_(req)

if res.card is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations

### [Wingspan SDK](docs/sdks/wingspan/README.md)

* [delete_payments_banking_card_id_](docs/sdks/wingspan/README.md#delete_payments_banking_card_id_) - delete a card by cardId
* [delete_payments_banking_instant_payout](docs/sdks/wingspan/README.md#delete_payments_banking_instant_payout) - delete instant payout
* [delete_payments_collaborator_settings_additional_data_id_](docs/sdks/wingspan/README.md#delete_payments_collaborator_settings_additional_data_id_) - Delete additional data
* [delete_payments_collaborator_settings_eligibility_requirement_id_](docs/sdks/wingspan/README.md#delete_payments_collaborator_settings_eligibility_requirement_id_) - Delete Eligibility Requirement
* [delete_payments_collaborator_settings_payment_eligibility_id_](docs/sdks/wingspan/README.md#delete_payments_collaborator_settings_payment_eligibility_id_) - Delete Payment Eligibility Requirement
* [delete_payments_payout_settings_member_id_debit_card_id_](docs/sdks/wingspan/README.md#delete_payments_payout_settings_member_id_debit_card_id_) - delete the payout debit card
* [get_payments](docs/sdks/wingspan/README.md#get_payments) - getServiceStatus
* [get_payments_banking_card](docs/sdks/wingspan/README.md#get_payments_banking_card) - list cards
* [get_payments_banking_instant_payout](docs/sdks/wingspan/README.md#get_payments_banking_instant_payout) - fetch instant payout details
* [get_payments_banking_institution_routing_number_](docs/sdks/wingspan/README.md#get_payments_banking_institution_routing_number_) - Get Institution By Routing Number
* [get_payments_banking_statement](docs/sdks/wingspan/README.md#get_payments_banking_statement) - list bank statements
* [get_payments_banking_statement_id_](docs/sdks/wingspan/README.md#get_payments_banking_statement_id_) - get bank statement
* [get_payments_banking_statement_id_download](docs/sdks/wingspan/README.md#get_payments_banking_statement_id_download) - download bank statement pdf
* [get_payments_bulk_payable_batch_batch_id_import_summary](docs/sdks/wingspan/README.md#get_payments_bulk_payable_batch_batch_id_import_summary) - Get Bulk Payable Batch Import Summary
* [get_payments_client_invoice_invoice_id_fees](docs/sdks/wingspan/README.md#get_payments_client_invoice_invoice_id_fees) - list client-invoice fees
* [get_payments_collaborator_settings_additional_data](docs/sdks/wingspan/README.md#get_payments_collaborator_settings_additional_data) - list additional settings
* [get_payments_collaborator_settings_additional_data_id_](docs/sdks/wingspan/README.md#get_payments_collaborator_settings_additional_data_id_) - Get additional data
* [get_payments_collaborator_settings_eligibility_requirement](docs/sdks/wingspan/README.md#get_payments_collaborator_settings_eligibility_requirement) - List Eligibility Requirements
* [get_payments_collaborator_settings_eligibility_requirement_id_](docs/sdks/wingspan/README.md#get_payments_collaborator_settings_eligibility_requirement_id_) - Get Eligibility Requirement
* [get_payments_collaborator_settings_payment_eligibility](docs/sdks/wingspan/README.md#get_payments_collaborator_settings_payment_eligibility) - List Payment Eligigbility Requirements
* [get_payments_collaborator_settings_payment_eligibility_id_](docs/sdks/wingspan/README.md#get_payments_collaborator_settings_payment_eligibility_id_) - Get Payment Eligibility Requirement
* [get_payments_collaborator_id_download_1099_year_index_](docs/sdks/wingspan/README.md#get_payments_collaborator_id_download_1099_year_index_) - Downloads a form 1099 PDF for a collaborator
* [get_payments_collaborator_id_download_w9](docs/sdks/wingspan/README.md#get_payments_collaborator_id_download_w9) - Downloads a form W9 PDF for a collaborator
* [get_payments_collaborator_id_events](docs/sdks/wingspan/README.md#get_payments_collaborator_id_events) - Get collaborator events by collaboratorId
* [get_payments_mcc](docs/sdks/wingspan/README.md#get_payments_mcc) - list mcc codes
* [get_payments_payout_settings_id_](docs/sdks/wingspan/README.md#get_payments_payout_settings_id_) - get the payout settings
* [get_payments_payout_settings_member_id_debit_card](docs/sdks/wingspan/README.md#get_payments_payout_settings_member_id_debit_card) - list the payout debit cards
* [get_payments_payout_settings_member_id_debit_card_id_](docs/sdks/wingspan/README.md#get_payments_payout_settings_member_id_debit_card_id_) - get the payout debit card
* [get_payments_service_banking_member_id_application](docs/sdks/wingspan/README.md#get_payments_service_banking_member_id_application) - gets an application link for creating the clearing bank account
* [get_payments_summary_payables](docs/sdks/wingspan/README.md#get_payments_summary_payables) - get payables summary
* [patch_payments_banking_card_id_](docs/sdks/wingspan/README.md#patch_payments_banking_card_id_) - update card by cardId
* [patch_payments_banking_card_id_token](docs/sdks/wingspan/README.md#patch_payments_banking_card_id_token) - exchange the code for a token
* [patch_payments_collaborator_settings_eligibility_requirement_id_](docs/sdks/wingspan/README.md#patch_payments_collaborator_settings_eligibility_requirement_id_) - Update Eligibility Requirement
* [post_payments_banking_card_id_token](docs/sdks/wingspan/README.md#post_payments_banking_card_id_token) - sends a verification code
* [post_payments_banking_instant_payout](docs/sdks/wingspan/README.md#post_payments_banking_instant_payout) - create instant payout details
* [post_payments_collaborator_settings_additional_data](docs/sdks/wingspan/README.md#post_payments_collaborator_settings_additional_data) - Create additional data
* [post_payments_collaborator_settings_eligibility_requirement](docs/sdks/wingspan/README.md#post_payments_collaborator_settings_eligibility_requirement) - Create Eligibility Requirement
* [post_payments_collaborator_settings_payment_eligibility](docs/sdks/wingspan/README.md#post_payments_collaborator_settings_payment_eligibility) - Create Payment Eligibility Requirement
* [post_payments_collaborator_1099_mark_undelivered](docs/sdks/wingspan/README.md#post_payments_collaborator_1099_mark_undelivered) - Mark a 1099 submission as returned by mail for collaborator
* [post_payments_collaborator_1099_remail](docs/sdks/wingspan/README.md#post_payments_collaborator_1099_remail) - Re-mail 1099 submission for collaborator
<!-- End SDK Available Operations -->

### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)

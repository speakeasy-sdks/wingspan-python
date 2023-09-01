# Petstore

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/wingspan-python.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->


```python
import petstore
from petstore.models import shared

s = petstore.Petstore()

req = shared.Mark1099AsUndeliveredRequest(
    member_id='corrupti',
    submission_index=5928.45,
    year=7151.9,
)

res = s.one_thousand_and_ninety_nine.mark(req)

if res.mark1099_as_undelivered_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [one_thousand_and_ninety_nine](docs/sdks/onethousandandninetynine/README.md)

* [mark](docs/sdks/onethousandandninetynine/README.md#mark) - Mark a 1099 submission as returned by mail for collaborator

### [additional_data](docs/sdks/additionaldata/README.md)

* [create](docs/sdks/additionaldata/README.md#create) - Create additional data
* [delete](docs/sdks/additionaldata/README.md#delete) - Delete additional data
* [get](docs/sdks/additionaldata/README.md#get) - Get additional data

### [additional_settings](docs/sdks/additionalsettings/README.md)

* [list](docs/sdks/additionalsettings/README.md#list) - List additional settings

### [app_link](docs/sdks/applink/README.md)

* [get](docs/sdks/applink/README.md#get) - Gets an application link for creating the clearing bank account

### [bank_statements](docs/sdks/bankstatements/README.md)

* [list](docs/sdks/bankstatements/README.md#list) - List bank statements

### [bulk_payable_batch_summary](docs/sdks/bulkpayablebatchsummary/README.md)

* [get](docs/sdks/bulkpayablebatchsummary/README.md#get) - Get Bulk Payable Batch Import Summary

### [card](docs/sdks/card/README.md)

* [delete](docs/sdks/card/README.md#delete) - Delete a card by cardId
* [update](docs/sdks/card/README.md#update) - Update card by cardId

### [cards](docs/sdks/cards/README.md)

* [list](docs/sdks/cards/README.md#list) - List cards

### [client_invoice_fees](docs/sdks/clientinvoicefees/README.md)

* [list](docs/sdks/clientinvoicefees/README.md#list) - List client-invoice fees

### [code_to_token](docs/sdks/codetotoken/README.md)

* [exchange](docs/sdks/codetotoken/README.md#exchange) - Exchange the code for a token

### [form1099](docs/sdks/form1099/README.md)

* [download](docs/sdks/form1099/README.md#download) - Downloads a form 1099 PDF for a collaborator

### [form_w9](docs/sdks/formw9/README.md)

* [download](docs/sdks/formw9/README.md#download) - Downloads a form W9 PDF for a collaborator

### [institution](docs/sdks/institution/README.md)

* [get](docs/sdks/institution/README.md#get) - Get Institution By Routing Number

### [mcc](docs/sdks/mcc/README.md)

* [list](docs/sdks/mcc/README.md#list) - List mcc codes

### [payables](docs/sdks/payables/README.md)

* [get](docs/sdks/payables/README.md#get) - Get payables summary

### [payment_eligibility_requirement](docs/sdks/paymenteligibilityrequirement/README.md)

* [create](docs/sdks/paymenteligibilityrequirement/README.md#create) - Create Payment Eligibility Requirement
* [delete](docs/sdks/paymenteligibilityrequirement/README.md#delete) - Delete Payment Eligibility Requirement
* [get](docs/sdks/paymenteligibilityrequirement/README.md#get) - Get Payment Eligibility Requirement

### [payment_eligibility_requirements](docs/sdks/paymenteligibilityrequirements/README.md)

* [list](docs/sdks/paymenteligibilityrequirements/README.md#list) - List Payment Eligigbility Requirements

### [service_status](docs/sdks/servicestatus/README.md)

* [get](docs/sdks/servicestatus/README.md#get) - Get Service Status

### [statement](docs/sdks/statement/README.md)

* [download](docs/sdks/statement/README.md#download) - Download bank statement pdf
* [get](docs/sdks/statement/README.md#get) - Get bank statement

### [verification](docs/sdks/verification/README.md)

* [send](docs/sdks/verification/README.md#send) - Sends a verification code
<!-- End SDK Available Operations -->

### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)

"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from typing import Optional
from wingspan import utils
from wingspan.models import errors, operations, shared

class BulkCalculation1099BatchItem:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def create(self, batch_id: str, bulk_calculation1099_item_create: Optional[shared.BulkCalculation1099ItemCreate] = None) -> operations.CreateBulkCalculation1099BatchItemResponse:
        r"""Create a bulk calculation1099 batch item"""
        request = operations.CreateBulkCalculation1099BatchItemRequest(
            batch_id=batch_id,
            bulk_calculation1099_item_create=bulk_calculation1099_item_create,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.CreateBulkCalculation1099BatchItemRequest, base_url, '/payments/bulk/calculation1099/batch/{batchId}/item', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "bulk_calculation1099_item_create", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateBulkCalculation1099BatchItemResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.BulkCalculation1099Item])
                res.bulk_calculation1099_item = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def get(self, batch_id: str, batch_item_id: str) -> operations.GetBulkCalculation1099BatchItemResponse:
        r"""Get a bulk calculation1099 batch item"""
        request = operations.GetBulkCalculation1099BatchItemRequest(
            batch_id=batch_id,
            batch_item_id=batch_item_id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetBulkCalculation1099BatchItemRequest, base_url, '/payments/bulk/calculation1099/batch/{batchId}/item/{batchItemId}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetBulkCalculation1099BatchItemResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.BulkCalculation1099Item])
                res.bulk_calculation1099_item = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def update(self, batch_id: str, batch_item_id: str, bulk_calculation1099_item_update: Optional[shared.BulkCalculation1099ItemUpdate] = None) -> operations.UpdateBulkCalculation1099BatchItemResponse:
        r"""Update a bulk calculation1099 batch item"""
        request = operations.UpdateBulkCalculation1099BatchItemRequest(
            batch_id=batch_id,
            batch_item_id=batch_item_id,
            bulk_calculation1099_item_update=bulk_calculation1099_item_update,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.UpdateBulkCalculation1099BatchItemRequest, base_url, '/payments/bulk/calculation1099/batch/{batchId}/item/{batchItemId}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "bulk_calculation1099_item_update", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateBulkCalculation1099BatchItemResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.BulkPayableItem])
                res.bulk_payable_item = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
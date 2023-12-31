"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from typing import Optional
from wingspan import utils
from wingspan.models import errors, operations, shared

class BulkPayableBatchItem:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def create(self, batch_id: str, bulk_payable_item_create: Optional[shared.BulkPayableItemCreate] = None) -> operations.CreateBulkPayableBatchItemResponse:
        r"""Create a bulk payable batch item"""
        request = operations.CreateBulkPayableBatchItemRequest(
            batch_id=batch_id,
            bulk_payable_item_create=bulk_payable_item_create,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.CreateBulkPayableBatchItemRequest, base_url, '/payments/bulk/payable/batch/{batchId}/item', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "bulk_payable_item_create", False, True, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateBulkPayableBatchItemResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.BulkPayableItem])
                res.bulk_payable_item = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def get(self, batch_id: str, batch_item_id: str) -> operations.GetBulkPayableBatchItemResponse:
        r"""Get a bulk payable batch item"""
        request = operations.GetBulkPayableBatchItemRequest(
            batch_id=batch_id,
            batch_item_id=batch_item_id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetBulkPayableBatchItemRequest, base_url, '/payments/bulk/payable/batch/{batchId}/item/{batchItemId}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetBulkPayableBatchItemResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.BulkPayableItem])
                res.bulk_payable_item = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def update(self, batch_id: str, batch_item_id: str, bulk_payable_item_update: Optional[shared.BulkPayableItemUpdate] = None) -> operations.UpdateBulkPayableBatchItemResponse:
        r"""Update a bulk payable batch item"""
        request = operations.UpdateBulkPayableBatchItemRequest(
            batch_id=batch_id,
            batch_item_id=batch_item_id,
            bulk_payable_item_update=bulk_payable_item_update,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.UpdateBulkPayableBatchItemRequest, base_url, '/payments/bulk/payable/batch/{batchId}/item/{batchItemId}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "bulk_payable_item_update", False, True, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.client
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateBulkPayableBatchItemResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.BulkPayableItem])
                res.bulk_payable_item = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
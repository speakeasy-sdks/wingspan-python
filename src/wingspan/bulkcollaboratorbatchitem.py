"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from typing import Optional
from wingspan import utils
from wingspan.models import errors, operations, shared

class BulkCollaboratorBatchItem:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def create(self, batch_id: str, bulk_collaborator_item_create: Optional[shared.BulkCollaboratorItemCreate] = None) -> operations.CreateBulkCollaboratorBatchItemResponse:
        r"""Create a bulk collaborator batch item"""
        request = operations.CreateBulkCollaboratorBatchItemRequest(
            batch_id=batch_id,
            bulk_collaborator_item_create=bulk_collaborator_item_create,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.CreateBulkCollaboratorBatchItemRequest, base_url, '/payments/bulk/collaborator/batch/{batchId}/item', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "bulk_collaborator_item_create", False, True, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateBulkCollaboratorBatchItemResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.BulkCollaboratorItem])
                res.bulk_collaborator_item = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def get(self, batch_id: str, batch_item_id: str) -> operations.GetBulkCollaboratorBatchItemResponse:
        r"""Get a bulk collaborator batch item"""
        request = operations.GetBulkCollaboratorBatchItemRequest(
            batch_id=batch_id,
            batch_item_id=batch_item_id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetBulkCollaboratorBatchItemRequest, base_url, '/payments/bulk/collaborator/batch/{batchId}/item/{batchItemId}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetBulkCollaboratorBatchItemResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.BulkCollaboratorItem])
                res.bulk_collaborator_item = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def update(self, batch_id: str, batch_item_id: str, bulk_collaborator_item_update: Optional[shared.BulkCollaboratorItemUpdate] = None) -> operations.UpdateBulkCollaboratorBatchItemResponse:
        r"""Update a bulk collaborator batch item"""
        request = operations.UpdateBulkCollaboratorBatchItemRequest(
            batch_id=batch_id,
            batch_item_id=batch_item_id,
            bulk_collaborator_item_update=bulk_collaborator_item_update,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.UpdateBulkCollaboratorBatchItemRequest, base_url, '/payments/bulk/collaborator/batch/{batchId}/item/{batchItemId}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "bulk_collaborator_item_update", False, True, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.client
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateBulkCollaboratorBatchItemResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.BulkCollaboratorItem])
                res.bulk_collaborator_item = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
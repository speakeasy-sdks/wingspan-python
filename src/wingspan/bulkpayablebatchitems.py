"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from typing import Optional
from wingspan import utils
from wingspan.models import errors, operations, shared

class BulkPayableBatchItems:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def list(self, batch_id: str) -> operations.ListBulkPayableBatchItemsResponse:
        r"""List bulk payable batch items"""
        request = operations.ListBulkPayableBatchItemsRequest(
            batch_id=batch_id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.ListBulkPayableBatchItemsRequest, base_url, '/payments/bulk/payable/batch/{batchId}/item', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListBulkPayableBatchItemsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.BulkPayableItem]])
                res.bulk_payable_items = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
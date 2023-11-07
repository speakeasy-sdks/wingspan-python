"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import card as shared_card
from ...models.shared import cardupdaterequest as shared_cardupdaterequest
from typing import Optional


@dataclasses.dataclass
class UpdateCardRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique identifier"""
    card_update_request: Optional[shared_cardupdaterequest.CardUpdateRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class UpdateCardResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    card: Optional[shared_card.Card] = dataclasses.field(default=None)
    r"""A card summary"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    


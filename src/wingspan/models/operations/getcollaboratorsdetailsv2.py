"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import collaboratorsreportresponse as shared_collaboratorsreportresponse
from typing import Optional



@dataclasses.dataclass
class GetCollaboratorsDetailsV2Response:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    collaborators_report_responses: Optional[list[shared_collaboratorsreportresponse.CollaboratorsReportResponse]] = dataclasses.field(default=None)
    r"""Collaborators list in the report"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    


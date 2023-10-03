"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import collaboratorevents as shared_collaboratorevents
from ..shared import redactedmember as shared_redactedmember
from ..shared import sixty_sixad6f986038e3285c36e0faa5c61b52a02882d1460acb116b601a30abfb6c1d as shared_sixty_sixad6f986038e3285c36e0faa5c61b52a02882d1460acb116b601a30abfb6c1d
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional, Union
from wingspan import utils



@dataclasses.dataclass
class CollaboratorsReportResponseLabels2:
    pass



@dataclasses.dataclass
class CollaboratorsReportResponseLabels:
    pass



@dataclasses.dataclass
class CollaboratorsReportResponseMemberEvents:
    pass

class StatusCollaboratorsReportResponse(str, Enum):
    ACTIVE = 'Active'
    INACTIVE = 'Inactive'
    PENDING = 'Pending'



@dataclasses.dataclass
class CollaboratorsReportResponseTaxDocumentStared:
    pass

class TaxStatusCollaboratorsReportResponse(str, Enum):
    COMPLETE = 'Complete'
    FAILED = 'Failed'
    PENDING = 'Pending'
    INCOMPLETE = 'Incomplete'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CollaboratorsReportResponse:
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientId') }})
    collaborator_groups: list[shared_sixty_sixad6f986038e3285c36e0faa5c61b52a02882d1460acb116b601a30abfb6c1d.SixtySixad6f986038e3285c36e0faa5c61b52a02882d1460acb116b601a30abfb6c1d] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collaboratorGroups') }})
    created_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt') }})
    invite_email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('inviteEmail') }})
    member: shared_redactedmember.RedactedMember = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('member') }})
    member_client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberClientId') }})
    member_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberId') }})
    status: StatusCollaboratorsReportResponse = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    tax_status: TaxStatusCollaboratorsReportResponse = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxStatus') }})
    updated_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt') }})
    external_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('externalId') }})
    labels: Optional[Union[Any, CollaboratorsReportResponseLabels2]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels'), 'exclude': lambda f: f is None }})
    member_events: Optional[Union[Any, shared_collaboratorevents.CollaboratorEvents]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberEvents'), 'exclude': lambda f: f is None }})
    tax_document_stared: Optional[Union[Any, bool]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxDocumentStared'), 'exclude': lambda f: f is None }})
    


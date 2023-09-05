"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from typing import Optional
from wingspan import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class InvoiceEvents:
    approved_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('approvedAt'), 'exclude': lambda f: f is None }})
    cancelled_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cancelledAt'), 'exclude': lambda f: f is None }})
    client_declined_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientDeclinedAt'), 'exclude': lambda f: f is None }})
    client_resolved_dispute_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientResolvedDisputeAt'), 'exclude': lambda f: f is None }})
    deposited_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('depositedAt'), 'exclude': lambda f: f is None }})
    deposited_to_payout_platform_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('depositedToPayoutPlatformAt'), 'exclude': lambda f: f is None }})
    disputed_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('disputedAt'), 'exclude': lambda f: f is None }})
    email_marked_as_spam_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('emailMarkedAsSpamAt'), 'exclude': lambda f: f is None }})
    email_received_at: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('emailReceivedAt'), 'exclude': lambda f: f is None }})
    email_undeliverable_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('emailUndeliverableAt'), 'exclude': lambda f: f is None }})
    email_viewed_at: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('emailViewedAt'), 'exclude': lambda f: f is None }})
    estimated_deposit_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('estimatedDepositAt'), 'exclude': lambda f: f is None }})
    instant_payout_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instantPayoutAt'), 'exclude': lambda f: f is None }})
    instant_payout_eligible_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instantPayoutEligibleAt'), 'exclude': lambda f: f is None }})
    instant_payout_failed_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instantPayoutFailedAt'), 'exclude': lambda f: f is None }})
    marked_paid_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('markedPaidAt'), 'exclude': lambda f: f is None }})
    member_accepted_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberAcceptedAt'), 'exclude': lambda f: f is None }})
    member_disputed_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberDisputedAt'), 'exclude': lambda f: f is None }})
    member_resubmitted_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberResubmittedAt'), 'exclude': lambda f: f is None }})
    opened_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('openedAt'), 'exclude': lambda f: f is None }})
    paid_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paidAt'), 'exclude': lambda f: f is None }})
    payment_failed_at: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paymentFailedAt'), 'exclude': lambda f: f is None }})
    payment_in_transit_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paymentInTransitAt'), 'exclude': lambda f: f is None }})
    payment_retried_at: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paymentRetriedAt'), 'exclude': lambda f: f is None }})
    payout_failed_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payoutFailedAt'), 'exclude': lambda f: f is None }})
    sent_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sentAt'), 'exclude': lambda f: f is None }})
    sent_due3_days_ago_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sentDue3DaysAgoAt'), 'exclude': lambda f: f is None }})
    sent_due7_days_ago_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sentDue7DaysAgoAt'), 'exclude': lambda f: f is None }})
    sent_due_in3_days_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sentDueIn3DaysAt'), 'exclude': lambda f: f is None }})
    sent_due_today_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sentDueTodayAt'), 'exclude': lambda f: f is None }})
    sent_instant_payout_failed_to_member: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sentInstantPayoutFailedToMember'), 'exclude': lambda f: f is None }})
    sent_manually_at: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sentManuallyAt'), 'exclude': lambda f: f is None }})
    sent_payment_confirmation_to_client: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sentPaymentConfirmationToClient'), 'exclude': lambda f: f is None }})
    sent_payment_confirmation_to_member: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sentPaymentConfirmationToMember'), 'exclude': lambda f: f is None }})
    sent_payment_in_transit_reminder_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sentPaymentInTransitReminderAt'), 'exclude': lambda f: f is None }})
    sent_recurring_payment_failed_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sentRecurringPaymentFailedAt'), 'exclude': lambda f: f is None }})
    

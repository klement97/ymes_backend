from typing import Optional

from django.utils import timezone

from apps.education.models.activity import Activity
from apps.organization.models import Organization


def get_current_activity(organization: Organization) -> Optional[Activity]:
    now = timezone.now()
    organization_activities = Activity.objects.filter(organization=organization)
    activity = organization_activities.filter(start_time__lte=now, end_time__gte=now)[:1]

    if activity.exists():
        return activity[0]

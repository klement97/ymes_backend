from typing import Optional

from django.utils import timezone

from apps.education.models.activity import Activity


def get_current_activity() -> Optional[Activity]:
    now = timezone.now()
    activity = Activity.objects.filter(start_time__lte=now, end_time__gte=now)[:1]

    if activity.exists():
        return activity[0]

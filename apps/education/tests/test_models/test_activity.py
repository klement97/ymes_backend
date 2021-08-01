from datetime import time
from unittest.mock import patch, MagicMock

import pytest
from django.db import IntegrityError
from model_bakery import baker

from apps.education.models.activity import get_current_activity, Activity

mock_timezone_path = 'apps.education.models.activity.timezone.now'
activity_model = 'education.Activity'


@pytest.mark.django_db
@patch(mock_timezone_path)
def test_get_current_activity_before_start(mock_timezone_now: MagicMock):
    start_time = time(10)
    baker.make(activity_model, start_time=start_time)
    time_before_earliest = time(hour=start_time.hour - 1)
    mock_timezone_now.return_value = time_before_earliest

    assert get_current_activity() is None


@pytest.mark.django_db
@patch(mock_timezone_path)
def test_get_current_activity_after_end(mock_timezone_now: MagicMock):
    end_time = time(17)
    baker.make(activity_model, end_time=end_time)
    time_after_last = time(hour=end_time.hour + 1)
    mock_timezone_now.return_value = time_after_last

    assert get_current_activity() is None


@pytest.mark.django_db
@patch(mock_timezone_path)
def test_get_current_activity_within_range(mock_timezone_now: MagicMock):
    activity_time = time(12, 0, 10)
    start_time = time(
        hour=activity_time.hour,
        minute=activity_time.minute,
        second=activity_time.second - 1
    )
    end_time = time(
        hour=activity_time.hour,
        minute=activity_time.minute,
        second=activity_time.second + 1
    )
    activity = baker.make(
        activity_model,
        start_time=start_time,
        end_time=end_time
    )

    mock_timezone_now.return_value = activity_time
    current_activity = get_current_activity()

    assert current_activity is not None
    assert current_activity.id == activity.id


def test_activity_ordering():
    assert Activity._meta.ordering == ['start_time'], \
        'Activities should be ordered by start time ascending'


@pytest.mark.django_db
def test_activity_str():
    activity = baker.make(activity_model)
    string_representation = str(activity)

    assert str(activity.start_time) in string_representation
    assert str(activity.end_time) in string_representation
    assert activity.name in string_representation


@pytest.mark.django_db
def test_can_not_create_activity_with_end_before_start():
    with pytest.raises(IntegrityError):
        Activity.objects.create(
            name='test',
            start_time=time(10),
            end_time=time(9)
        )

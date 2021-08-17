from datetime import time
from unittest.mock import patch, MagicMock

import pytest
from model_bakery import baker

from apps.education.tests.utils import mock_timezone_path, organization_model, activity_model
from apps.education.utils.activity import get_current_activity


@pytest.mark.django_db
@patch(mock_timezone_path)
def test_get_current_activity_before_start(mock_timezone_now: MagicMock):
    organization = baker.make(organization_model)
    start_time = time(10)
    baker.make(
        activity_model,
        start_time=start_time,
        end_time=time(11),
        organization=organization
    )
    time_before_earliest = time(hour=start_time.hour - 1)
    mock_timezone_now.return_value = time_before_earliest

    assert get_current_activity(organization) is None


@pytest.mark.django_db
@patch(mock_timezone_path)
def test_get_current_activity_after_end(mock_timezone_now: MagicMock):
    organization = baker.make(organization_model)
    end_time = time(17)
    baker.make(
        activity_model,
        start_time=time(16),
        end_time=end_time,
        organization=organization
    )
    time_after_last = time(hour=end_time.hour + 1)
    mock_timezone_now.return_value = time_after_last

    assert get_current_activity(organization) is None


@pytest.mark.django_db
@patch(mock_timezone_path)
def test_get_current_activity_within_range(mock_timezone_now: MagicMock):
    organization = baker.make(organization_model)
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
        end_time=end_time,
        organization=organization
    )

    mock_timezone_now.return_value = activity_time
    current_activity = get_current_activity(organization)

    assert current_activity is not None
    assert current_activity.id == activity.id

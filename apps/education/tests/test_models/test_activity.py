from datetime import time

import pytest
from django.db import IntegrityError
from model_bakery import baker

from apps.education.models.activity import Activity
from apps.education.tests.utils import activity_model


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

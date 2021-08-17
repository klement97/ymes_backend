from unittest.mock import patch, MagicMock

import pytest
from django.contrib.auth import get_user_model
from model_bakery import baker
from rest_framework import status

from apps.education.tests.utils import (
    mock_get_current_activity,
    current_activity_url,
    activity_model,
    activity_url,
    organization_model
)


@patch(mock_get_current_activity)
@pytest.mark.django_db
def test_current_activity_when_no_activity_found(mock: MagicMock, api_client):
    mock.return_value = None
    response = api_client.get(current_activity_url)

    assert response.status_code == status.HTTP_200_OK
    assert 'error' in response.data


@patch(mock_get_current_activity)
@pytest.mark.django_db
def test_current_activity_when_no_activity_found(mock: MagicMock, api_client):
    activity = baker.make(activity_model)
    mock.return_value = activity
    response = api_client.get(current_activity_url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data['id'] == activity.id


@pytest.mark.django_db
def test_get_activities_when_not_in_organization(api_client):
    baker.make(activity_model, _quantity=20)
    response = api_client.get(activity_url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 0


@pytest.mark.django_db
def test_get_activities_when_in_another_organization(custom_api_client):
    user = baker.make(get_user_model())
    user.organization = baker.make(organization_model)
    user.save()
    another_organization = baker.make(organization_model)

    baker.make(activity_model, organization=user.organization, _quantity=5)
    baker.make(activity_model, organization=another_organization, _quantity=10)

    client = custom_api_client(user)
    response = client.get(activity_url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 5

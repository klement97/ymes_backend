from unittest.mock import patch, MagicMock

import pytest
from model_bakery import baker
from rest_framework import status


@patch('apps.education.views.activity.get_current_activity')
@pytest.mark.django_db
def test_current_activity_when_no_activity_found(mock: MagicMock, api_client):
    mock.return_value = None
    response = api_client.get('/activity/current/')

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data is None


@patch('apps.education.views.activity.get_current_activity')
@pytest.mark.django_db
def test_current_activity_when_no_activity_found(mock: MagicMock, api_client):
    activity = baker.make('education.Activity')
    mock.return_value = activity
    response = api_client.get('/activity/current/')

    assert response.status_code == status.HTTP_200_OK
    assert response.data['id'] == activity.id
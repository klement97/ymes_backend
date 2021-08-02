import pytest
from faker import Faker
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from apps.authentication.models import User

fake = Faker()


@pytest.fixture()
def api_client() -> APIClient:
    # Include an appropriate `Authorization:` header on all requests.
    user, created = User.objects.get_or_create(phone_number=fake.phone_number())
    token, created = Token.objects.get_or_create(user=user)
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    return client

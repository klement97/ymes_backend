import pytest
from django.contrib.auth import get_user_model
from faker import Faker

fake = Faker()


@pytest.mark.django_db
def test_create_user_with_valid_fields():
    """
    Ensure the user is created with valid config fields.
    Values must be:
        phone_number: set
        is_active:    True
        is_staff:     False
        is_superuser: False
    """
    user_manager = get_user_model().objects
    phone_number = fake.phone_number()
    user = user_manager.create_user(phone_number=phone_number, password='foo')

    assert user.phone_number == phone_number
    assert user.is_active
    assert not user.is_staff
    assert not user.is_superuser


@pytest.mark.django_db
def test_username_is_not_used():
    user_manager = get_user_model().objects
    user = user_manager.create_user(phone_number=fake.phone_number(),
                                    password='foo')
    try:
        assert user.username is None

    except AttributeError:
        pass


@pytest.mark.django_db
def test_if_raises_exception_when_needed():
    user_manager = get_user_model().objects
    user_manager.create_user(phone_number=fake.phone_number(), password='foo')

    with pytest.raises(TypeError):
        user_manager.create_user()

    with pytest.raises(TypeError):
        user_manager.create_user(email='')

    with pytest.raises(ValueError):
        user_manager.create_user(phone_number='', password="foo")


@pytest.mark.django_db
def test_create_superuser_valid_fields():
    user_manager = get_user_model().objects
    phone_number = fake.phone_number()
    admin_user = user_manager.create_superuser(
        phone_number=phone_number,
        password='foo'
    )

    assert admin_user.phone_number == phone_number
    assert admin_user.is_active
    assert admin_user.is_staff
    assert admin_user.is_superuser


@pytest.mark.django_db
def test_create_super_user_not_valid_fields():
    with pytest.raises(ValueError):
        get_user_model().objects.create_superuser(
            phone_number=fake.phone_number(),
            password='foo',
            is_superuser=False
        )

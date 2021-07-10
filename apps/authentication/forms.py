from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from apps.authentication.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'

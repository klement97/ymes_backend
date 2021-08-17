from rest_framework.serializers import ModelSerializer

from apps.education.models import MealMenu


class MealMenuSerializer(ModelSerializer):
    class Meta:
        model = MealMenu
        fields = '__all__'

from rest_framework.serializers import ModelSerializer

from apps.education.models import WeekMenu


class WeekMenuSerializer(ModelSerializer):
    class Meta:
        model = WeekMenu
        fields = '__all__'

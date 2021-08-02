from rest_framework.serializers import ModelSerializer

from apps.education.models.activity import Activity


class ActivitySerializer(ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

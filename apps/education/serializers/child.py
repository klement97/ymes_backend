from rest_framework.serializers import ModelSerializer

from apps.education.models import Child


class ChildSerializer(ModelSerializer):
    class Meta:
        model = Child
        exclude = ['created_at', 'updated_at', 'is_deleted']

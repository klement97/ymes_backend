from rest_framework.viewsets import ModelViewSet

from apps.common.permissions import IsAdmin, ReadOnly
from apps.education.models import Child
from apps.education.serializers.child import ChildSerializer


class ChildViewSet(ModelViewSet):
    serializer_class = ChildSerializer
    permission_classes = [IsAdmin | ReadOnly]
    queryset = Child.objects \
        .prefetch_related('parents') \
        .filter(is_deleted=False)

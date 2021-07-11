from rest_framework.viewsets import ViewSet

from apps.education.models import Child
from apps.education.serializers.child import ChildSerializer


class ChildViewSet(ViewSet):
    queryset = Child.objects.prefetch_related('parents').filter(
        is_deleted=False)
    serializer_class = ChildSerializer

    def list(self):
        queryset = self.queryset.filter()

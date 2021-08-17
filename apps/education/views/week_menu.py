from rest_framework.viewsets import ModelViewSet

from apps.common.permissions import IsAdmin, ReadOnly
from apps.education.models import WeekMenu
from apps.education.serializers.week_menu import WeekMenuSerializer


class WeekMenuViewSet(ModelViewSet):
    serializer_class = WeekMenuSerializer
    permission_classes = [IsAdmin | ReadOnly]
    queryset = WeekMenu.objects.all()

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(organization_id=user.organization_id)

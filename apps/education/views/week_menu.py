from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.common.permissions import IsAdmin, AuthenticatedReadOnly
from apps.education.models import WeekMenu
from apps.education.serializers.week_menu import WeekMenuSerializer, WeekMenuMealsSerializer


class WeekMenuViewSet(ModelViewSet):
    serializer_class = WeekMenuSerializer
    permission_classes = [IsAdmin | AuthenticatedReadOnly]
    queryset = WeekMenu.objects.all()

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(organization_id=user.organization_id)

    @action(
        detail=False,
        description='Get the active Week Menu'
    )
    def active(self, request):
        try:
            week_menu = self.get_queryset().get(is_active=True)
            data = WeekMenuMealsSerializer(instance=week_menu).data

            return Response(data)

        except WeekMenu.DoesNotExist:
            return Response(
                data={'message': 'No menu found!'},
                status=status.HTTP_400_BAD_REQUEST
            )

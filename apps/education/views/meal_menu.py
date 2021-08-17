from rest_framework.viewsets import ModelViewSet

from apps.common.permissions import IsAdmin, AuthenticatedReadOnly
from apps.education.models import MealMenu
from apps.education.serializers.meal_menu import MealMenuSerializer


class MealMenuViewSet(ModelViewSet):
    serializer_class = MealMenuSerializer
    permission_classes = [IsAdmin | AuthenticatedReadOnly]
    queryset = MealMenu.objects.all()

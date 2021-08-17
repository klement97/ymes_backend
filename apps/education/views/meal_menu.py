from rest_framework.viewsets import ModelViewSet

from apps.common.permissions import IsAdmin, ReadOnly
from apps.education.models import MealMenu
from apps.education.serializers.meal_menu import MealMenuSerializer


class MealMenuViewSet(ModelViewSet):
    serializer_class = MealMenuSerializer
    permission_classes = [IsAdmin | ReadOnly]
    queryset = MealMenu.objects.all()

from rest_framework.routers import DefaultRouter

from apps.education.views.activity import ActivityViewSet
from apps.education.views.child import ChildViewSet
from apps.education.views.meal_menu import MealMenuViewSet
from apps.education.views.week_menu import WeekMenuViewSet

router = DefaultRouter()
router.register('activity', ActivityViewSet, basename='activity')
router.register('child', ChildViewSet, basename='child')
router.register('meal-menu', MealMenuViewSet, basename='meal-menu')
router.register('week-menu', WeekMenuViewSet, basename='week-menu')

urlpatterns = router.urls

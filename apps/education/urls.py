from rest_framework.routers import SimpleRouter

from apps.education.views.child import ChildViewSet

router = SimpleRouter()
router.register('child', ChildViewSet)

urlpatterns = router.urls

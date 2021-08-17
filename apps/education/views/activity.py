from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.common.permissions import IsAdmin, AuthenticatedReadOnly
from apps.education.models.activity import Activity
from apps.education.serializers.activity import ActivitySerializer
from apps.education.utils.activity import get_current_activity


class ActivityViewSet(ModelViewSet):
    serializer_class = ActivitySerializer
    permission_classes = [IsAdmin | AuthenticatedReadOnly]
    queryset = Activity.objects.all()

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(organization_id=user.organization_id)

    @action(
        detail=False,
        description='Get the activity which is happening right now if any.'
    )
    def current(self, request):
        data = None
        if activity := get_current_activity(request.user.organization):
            serializer = ActivitySerializer(instance=activity)
            data = serializer.data

        return Response(data=data)

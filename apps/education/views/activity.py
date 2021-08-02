from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from apps.education.models.activity import Activity
from apps.education.serializers.activity import ActivitySerializer
from apps.education.utils.activity import get_current_activity


class ActivityListView(ListAPIView):
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()


activity_list_view = ActivityListView.as_view()


@api_view()
def current_activity(_):
    if activity := get_current_activity():
        serializer = ActivitySerializer(instance=activity)

        return Response(data=serializer.data)

    return Response(status=status.HTTP_404_NOT_FOUND)

from rest_framework.generics import ListAPIView

from apps.education.models import Child
from apps.education.serializers.child import ChildSerializer


class ChildListView(ListAPIView):
    serializer_class = ChildSerializer
    queryset = Child.objects \
        .prefetch_related('parents') \
        .filter(is_deleted=False)


child_list_view = ChildListView.as_view()

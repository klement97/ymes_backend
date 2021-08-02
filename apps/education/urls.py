from django.urls import path

from apps.education.views.activity import activity_list_view, current_activity
from apps.education.views.child import child_list_view

urlpatterns = [
    path('child/', child_list_view),
    path('activity/', activity_list_view),
    path('activity/current/', current_activity)
]

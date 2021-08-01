from django.urls import path

from apps.education.views.child import child_view

urlpatterns = [
    path('child/', child_view)
]

from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('token/', views.obtain_auth_token),
]

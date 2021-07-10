from django.urls import path
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

swagger = SpectacularSwaggerView.as_view(url_name='schema')

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', swagger, name='swagger-ui'),
]

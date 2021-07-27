from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='reviews:api-root')),
    path('api/', include('reviews.urls', namespace='reviews')),
    path('api/auth/', include('rest_framework.urls')),
    path('api/auth/', include('accounts.urls')),
]

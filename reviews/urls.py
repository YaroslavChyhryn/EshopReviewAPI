from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'reviews'

router = DefaultRouter()
router.register(r'reviews', views.ReviewViewSet, basename='reviews')

urlpatterns = [
    path('', include(router.urls)),
    path('shops', views.ShopView.as_view(), name='shops'),
    path('reviews/by_user', views.UserReviewView.as_view(), name='by_user'),
]

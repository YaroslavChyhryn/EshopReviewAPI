from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('register', views.CreateUserView.as_view(), name='register'),
    path('token', views.UserToken.as_view(), name='token'),
]

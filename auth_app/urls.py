from django.urls import path
from auth_app import views


# URL Configuration for auth_app
app_name='auth_app'

urlpatterns = [
    path('register/', views.RegisterAPIView.as_view(), name='user_register'),
]

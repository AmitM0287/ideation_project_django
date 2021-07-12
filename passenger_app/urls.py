from django.urls import path
from passenger_app import views


# URL Configuration for auth_app
app_name='passenger_app'

urlpatterns = [
    path('data/', views.PassengerAPIView.as_view(), name='passenger_data'),
]

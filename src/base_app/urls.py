from django.urls import path

from . import views

app_name = 'base_app'

urlpatterns = [
    path('registration/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.GenerateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
]
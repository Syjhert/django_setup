from django.urls import path
from . import views

urlpatterns = [
    path('', views.gateway_view, name='gateway_view'),
    path('login/', views.login_view, name='login_view'),
    path('signup/', views.signup_view, name='signup_view'),
]
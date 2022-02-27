from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name="hello-world"),
    path('token/', views.token, name="token"),
    path('login/', views.login, name="login"),
    path('registration/', views.registration, name="registration"),
]
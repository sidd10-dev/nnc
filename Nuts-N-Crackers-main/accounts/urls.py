from django.shortcuts import redirect
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

app_name = "accounts"

urlpatterns = [
    path('signup/',views.signup,name = 'signup'),
    path('userlogin/',views.userlogin,name = 'userlogin'),
    path('logout/',LogoutView.as_view(),name = 'logout')
]
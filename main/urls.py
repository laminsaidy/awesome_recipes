"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_Views
from django.views.generic.base import TemplateView



urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', include('recipes.urls')),
    path('register/', user_views.register, name="user-register"),
    path('login/', auth_Views.LoginView.as_view(template_name='users/login.html'), name="user-login"),
    path('logout/', auth_Views.LogoutView.as_view(template_name='users/logout.html'), name="user-logout"),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path('profile/', user_views.profile, name="user-profile"),

    
]

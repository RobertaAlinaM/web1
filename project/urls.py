"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),  # Create a new path for the home page
    path("accounts/", include("accounts.urls")),  # It is very important to include this BEFORE the built-in authentication URLs
    path("accounts/", include("django.contrib.auth.urls")),  # Add the path for the built-in authentication URLs
    path("plane/", TemplateView.as_view(template_name="plane.html"), name="plane"),
    path("subway/", TemplateView.as_view(template_name="subway.html"), name="subway"),
    path("car/", TemplateView.as_view(template_name="car/car.html"), name="car"),
    path("boat/", TemplateView.as_view(template_name="boat.html"), name="boat"),
    path("train/", TemplateView.as_view(template_name="train.html"), name="train"),
    path("motorbike/", TemplateView.as_view(template_name="motorbike.html"), name="motorbike"),

]

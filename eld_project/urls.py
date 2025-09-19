"""
URL configuration for eld_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.shortcuts import render

urlpatterns = [
    # 🌟 Homepage with animated welcome screen
    path('', lambda request: render(request, 'home.html')),

    # 🔗 API routes (replace 'your_api_app' with your actual app name)
    path('api/', include('eld_api.urls')),

    # 🛠 Django admin panel
    path('admin/', admin.site.urls),
]


"""netflix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.shortcuts import redirect

def developer(request):
    return redirect("https://eitozx.github.io")

def donate(request):
    return redirect("https://ko-fi.com/EitoZX")

def project(request):
    return redirect("https://github.com/EitoZX/Netflix-Clone")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    
    path('', include('core.urls')),

    path('developer/', developer, name='developer'),
    path('donate/', donate, name='donate'),
    path('project/', project, name = 'project')
]

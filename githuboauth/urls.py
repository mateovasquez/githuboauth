"""
URL configuration for githuboauth project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path

from githuboauth.views import home_view
from user_profile.views import (
    user_detail_view,
    profile_edit_view,
    profile_detail_view,
    profile_delete_view,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    
    path('', home_view, name="home"),
    path('user', user_detail_view, name='user_detail'),
    path('profile', profile_detail_view, name='profile_detail'),
    path('profile-edit', profile_edit_view, name='profile_edit'),
    path('profile-delete', profile_delete_view, name='profile_delete'),
]

"""BauJo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from .views import page_home, page_profile, page_key, page_today, page_this_week, page_today, KeyListView, new_key

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', page_home, name = 'home'),
    path('home/', page_home, name = 'home'),
    path('profile/', page_profile, name = 'profile'),
    path('key/', KeyListView.as_view(), name = 'key'),
    path('this_week/', page_this_week, name = 'this_week'),
    path('today/', page_today, name = 'today'),
    path('new_key/', new_key, name = 'new_key'),

]

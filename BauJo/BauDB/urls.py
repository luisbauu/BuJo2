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
from django.conf import settings
from django.conf.urls.static import static

#from .views import page_home, page_profile, page_key, page_today, page_this_week, page_today, KeyListView, new_key, ProfileDetailView, ProfileNameView, ProfileBioView
from .views import *

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', page_home, name = 'home'),
    path('home/', page_home, name = 'home'),
    path('profile/', ProfileDetailView.as_view(), name = 'profile'),
    path('key/', KeyListView.as_view(), name = 'key'),
    path('this_week/', thisWeekListView.as_view(), name = 'this_week'),
    path('today/', TodayListView.as_view(), name = 'today'),
    path('new_key/', new_key, name = 'new_key'),
    path('new_today/', new_today, name = 'new_today'),
    path('new_thisWeek/', new_thisWeek, name ='new_thisWeek'),
    path('new_name/',ProfileNameView.as_view(), name = 'new_name'),
    path('new_bio/',ProfileBioView.as_view(), name = 'new_bio'), 
    path('new_image/',ProfileImageView.as_view(), name = 'new_image'),
    path('new_today_update/<int:pk>/',TodayUpdateView.as_view(), name = 'new_today_update'), 
    path('today_delete/<int:pk>/',TodayDeleteView.as_view(), name = 'today_delete'),
    path('today_done/<int:pk>/',page_today_done, name = 'today_done'),
    path('new_thisWeek_update/<int:pk>/',thisWeekUpdateView.as_view(), name = 'new_thisWeek_update'), 
    path('thisWeek_delete/<int:pk>/',thisWeekDeleteView.as_view(), name = 'thisWeek_delete'),
    path('thisWeek_done/<int:pk>/',page_thisWeek_done, name = 'thisWeek_done'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

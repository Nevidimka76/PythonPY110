"""
URL configuration for project project.

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
from django.urls import path, include
# from django.urls import path,re_path
# from random import random
# from django.http import HttpResponse
# from app_datetime.views import datetime_view, dateView, fileView


# def random_view(request):
#     if request.method == "GET":
#         data = random()
#         return HttpResponse(data)
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('weather/',include('app_weather.urls')),
    path('',include('store.urls')),
    path('login/', include('app_login.urls')),    
    path('wishlist/', include('wishlist.urls')),    
    # path('random/', random_view),
    # path('file/', fileView),
    # path('datetime/', datetime_view),
    # re_path(r'^json/(?P<d>[0-9]{1,2})/(?P<m>[0-9]{1,2})/(?P<year>[0-9]{4})/$', dateView.as_view()),
    # #path('datetime/json/<int:year>/', dateView.as_view()),
    # path('datetime/json/', dateView.as_view()),
]

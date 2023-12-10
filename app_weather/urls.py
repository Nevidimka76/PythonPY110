from django.urls import path,re_path
from .views import viewCurrentWeather


    
urlpatterns = [
#    re_path(r'^json/(?P<d>[0-9]{1,2})/(?P<m>[0-9]{1,2})/(?P<year>[0-9]{4})/$', dateView.as_view()),
    path('weather/<str:lat>/<str:lon>/', viewCurrentWeather.as_view()),
] 
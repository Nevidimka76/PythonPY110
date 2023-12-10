from django.urls import path,re_path
from .views import datetime_view, dateView, fileView, random_view


    
urlpatterns = [
    path('random/', random_view), 
    path('file/', fileView),
    path('datetime/', datetime_view),
    re_path(r'^json/(?P<d>[0-9]{1,2})/(?P<m>[0-9]{1,2})/(?P<year>[0-9]{4})/$', dateView.as_view()),
    #path('datetime/json/<int:year>/', dateView.as_view()),
    path('json/', dateView.as_view()),
] 
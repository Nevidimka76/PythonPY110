from django.urls import path,re_path
from .views import productsView,shopView,productsPageView,cartView,cartDelView,cartAddView

app_name='store'
    
urlpatterns = [
#    re_path(r'^json/(?P<d>[0-9]{1,2})/(?P<m>[0-9]{1,2})/(?P<year>[0-9]{4})/$', dateView.as_view()),
    path('product/', productsView.as_view()),
    path('',shopView.as_view(), name="shopView"),
    path('product/<slug:page>.html',productsPageView.as_view(), name='productsPageView'),
    path('product/<int:page>', productsPageView.as_view(), name='productsPageViewInt'),
    path('cart/', cartView.as_view()),
    path('cart/add/<str:idProduct>', cartAddView.as_view()),
    path('cart/del/<str:idProduct>', cartDelView.as_view()),
] 
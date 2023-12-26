from django.urls import path,re_path
from .views import productsView,shopView,productsPageView,cartView,\
                    cartDelView,cartAddView,couponСheckView, deliveryEstimateView,\
                    cartBuyNowView,cartRemoveView

app_name='store'
    
urlpatterns = [
#    re_path(r'^json/(?P<d>[0-9]{1,2})/(?P<m>[0-9]{1,2})/(?P<year>[0-9]{4})/$', dateView.as_view()),
    path('product/', productsView.as_view()),
    path('',shopView.as_view(), name="shopView"),
    path('product/<slug:page>.html',productsPageView.as_view(), name='productsPageView'),
    path('product/<int:page>', productsPageView.as_view(), name='productsPageViewInt'),
    path('cart/', cartView.as_view(),name='cartView'),
    path('cart/add/<str:idProduct>', cartAddView.as_view()),
    path('cart/del/<str:idProduct>', cartDelView.as_view()),
    path('delivery/estimate/', deliveryEstimateView.as_view()),
    path("coupon/check/<slug:name_coupon>", couponСheckView.as_view()),
    path('cart/buy/<str:idProduct>', cartBuyNowView.as_view(), name="buyNow"),
    path('cart/remove/<str:idProduct>', cartRemoveView.as_view(), name="removeNow"),
] 
from django.urls import path
from .views import wishlistView,wishlistAddView,wishlistDelView,wishlistJSON,wishRemoveView


app_name='wishlist'

urlpatterns = [
    path('',wishlistView.as_view(), name='wishList'),  # TODO Зарегистрируйте обработчик
    path('api/add/<str:idProduct>', wishlistAddView.as_view(), name='wishlist_add_json'),
    path('api/del/<str:idProduct>', wishlistDelView.as_view(), name='wishlist_del_json'),
    path('api/',wishlistJSON.as_view(), name='wishlist_json'),  # TODO Зарегистрируйте обработчик
    path('api/remove/<str:idProduct>',wishRemoveView.as_view(), name='removeNow'),  # TODO Зарегистрируйте обработчик
]
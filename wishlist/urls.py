from django.urls import path
from .views import wishlistView

app_name='wishlist'

urlpatterns = [
    path('',wishlistView.as_view(), name='wishList'),  # TODO Зарегистрируйте обработчик
]
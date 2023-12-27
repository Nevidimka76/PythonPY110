from django.urls import path
from .views import loginView, logoutView

app_name = 'login'

urlpatterns = [
    path('', loginView.as_view(), name="login_view"),
    path('logout/', logoutView.as_view(), name="logout_view"),
]
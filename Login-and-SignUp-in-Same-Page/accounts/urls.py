from django.urls import path
from .import views

urlpatterns = [
    path('index',views.index, name="index_url"),
    path('login',views.Login, name="login_url"),
    path('register',views.Register, name="register_url"),
    path('logout',views.logout, name="logout_url")
]
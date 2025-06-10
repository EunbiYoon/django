"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from main.views import homeView
from users.views import loginView, registerView, logoutView
from sections.views import detailView, categoryView, DeletePostView

urlpatterns = [
    #admin
    path('admin/', admin.site.urls),

    #main
    path('', homeView, name='home_url'),

    #users
    path('login/',loginView, name="login_url"),
    path('register/',registerView, name="register_url"),
    path('logout/',logoutView, name="logout_url"),

    # dtail
    path('<slug:slug>/', categoryView, name='category_url'),
    path('<slug:slug>/<int:pk>/', detailView, name='detail_url'),
    path('delete/<int:pk>/', DeletePostView.as_view(), name="delete_post"),

]

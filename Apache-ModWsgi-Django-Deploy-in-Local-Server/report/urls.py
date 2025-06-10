from django.urls import path
from .views import home_view, detail_bom_view, detail_cost_view, category_bom_view, category_cost_view

urlpatterns = [
    # detail
    path('',home_view,name='home_url'),
    path('1-<slug:slug>/<int:pk>', detail_bom_view, name='detail_bom_url'),
    path('2-<slug:slug>/<int:pk>', detail_cost_view, name='detail_cost_url'),
    path('1-<slug:slug>', category_bom_view, name='category_bom_url'),
    path('2-<slug:slug>', category_cost_view, name='category_cost_url'),
]

from django.urls import path
from django.views.decorators.cache import cache_page

from . import views


app_name = 'product'

urlpatterns = [

    path('list/', views.ProductListView.as_view(),
         name='product-list'),

    path('<slug:slug>/', views.ProductDetailView.as_view(),
         name='product-detail'),

]

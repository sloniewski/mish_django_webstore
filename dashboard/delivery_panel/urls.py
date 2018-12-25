from django.urls import path

from . import views


app_name = 'delivery_panel'

urlpatterns = [

    # Delivery
    path('list/', views.DeliveryListView.as_view(),
         name='delivery-list'),

    path('update/<pk>', views.DeliveryUpdateView.as_view(),
         name='delivery-update'),

    # delivery pricing
    path('option-list/', views.DeliveryPricingListView.as_view(),
         name='delivery-option-list'),

    path('option/<int:pk>/update', views.DeliveryPricingUpdateView.as_view(),
         name='delivery-option-update'),

    path('option/<int:pk>/delete', views.DeliveryPricingDeleteView.as_view(),
         name='delivery-option-delete'),

    path('option/create', views.DeliveryPricingCreateView.as_view(),
         name='delivery-option-create'),

]

from django.urls import path

from . import views


app_name = 'order_panel'

urlpatterns = [
    
    # Order
    path('list', views.OrderListView.as_view(),
         name='order-list'),

    path('<int:pk>', views.OrderDetailView.as_view(),
         name='order-detail'),


    path('update/<uuid>', views.OrderUpdateView.as_view(),
         name='order-update'),

    # OrderItem
    path('update/item/<pk>', views.OrderItemUpdateView.as_view(),
         name='order-item-update'),

    path('delete/item/<pk>', views.OrderItemDeleteView.as_view(),
         name='order-item-delete'),

]

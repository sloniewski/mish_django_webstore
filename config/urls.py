"""mish_django_webstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from webstore.core.views import WelcomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/doc/', include('django.contrib.admindocs.urls')),

    path('product/', include('webstore.product.urls')),
    path('cart/', include('webstore.cart.urls')),
    path('order/', include('webstore.order.urls')),
    path('users/', include('webstore.users.urls')),
    path('payment/', include('webstore.payment.urls')),

    path('dashboard/product_panel/', include('dashboard.product_panel.urls')),
    path('dashboard/order_panel/', include('dashboard.order_panel.urls')),
    path('dashboard/payment_panel/', include('dashboard.payment_panel.urls')),
    path('dashboard/delivery_panel/', include('dashboard.delivery_panel.urls')),
    path('dashboard/users_panel/', include('dashboard.users_panel.urls')),

    path('', WelcomeView.as_view(), name="welcome"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

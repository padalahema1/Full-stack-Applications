from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('restaurants/', views.restaurant_list, name='restaurants'),

    path('menu/<int:id>/', views.menu, name='menu'),

    path('order/<int:id>/', views.place_order, name='place_order'),

    path('orders/', views.orders, name='orders'),

    path('payment/<int:order_id>/', views.payment_view, name='payment'),

    path(
        'payment-success/<int:order_id>/',
        views.payment_success,
        name='payment_success'
    ),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
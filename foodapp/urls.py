from django.urls import path
from . import views


urlpatterns = [

    path(
        "",
        views.home,
        name="home"
    ),

    path(
        "restaurants/",
        views.restaurant_list,
        name="restaurant_list"
    ),

    path(
        "menu/<int:restaurant_id>/",
        views.menu,
        name="menu"
    ),

    path(
        "order/<int:id>/",
        views.place_order,
        name="place_order"
    ),

    path(
        "orders/",
        views.order_list,
        name="order_list"
    ),

    path(
        "payment/<int:order_id>/",
        views.payment_view,
        name="payment"
    ),

    path(
        "payment-success/<int:order_id>/",
        views.payment_success,
        name="payment_success"
    ),
    path(
        "payment/<int:order_id>/",
        views.payment,
        name="payment"
    ),

    path(
        "payment-success/<int:order_id>/",
        views.payment_success,
        name="payment_success"
    ),

]


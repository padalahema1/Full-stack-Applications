from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from pathlib import Path

import qrcode

from .models import Restaurant, MenuItem, Order


def home(request):

    restaurants = Restaurant.objects.all()

    return render(
        request,
        "foodapp/home.html",
        {
            "restaurants": restaurants
        }
    )


def restaurant_list(request):

    restaurants = Restaurant.objects.all()

    return render(
        request,
        "foodapp/restaurants.html",
        {
            "restaurants": restaurants
        }
    )


def menu(request, restaurant_id):

    restaurant = get_object_or_404(
        Restaurant,
        id=restaurant_id
    )

    items = MenuItem.objects.filter(
        restaurant=restaurant
    )

    return render(
        request,
        "foodapp/menu.html",
        {
            "restaurant": restaurant,
            "items": items
        }
    )


def place_order(request, id):

    item = get_object_or_404(
        MenuItem,
        id=id
    )

    if request.method == "POST":

        customer_name = request.POST.get(
            "customer_name",
            "Guest"
        ).strip()

        if not customer_name:
            customer_name = "Guest"

        try:
            quantity = int(
                request.POST.get(
                    "quantity",
                    1
                )
            )
        except (ValueError, TypeError):

            quantity = 1

        if quantity < 1:
            quantity = 1

        total = item.price * quantity

        order = Order.objects.create(
            item=item,
            customer_name=customer_name,
            quantity=quantity,
            total_price=total,
            status="Pending"
        )

        return redirect(
            "payment",
            order_id=order.id
        )

    return render(
        request,
        "foodapp/order.html",
        {
            "item": item
        }
    )


def order_list(request):

    orders = Order.objects.select_related(
        "item",
        "item__restaurant"
    ).order_by("-created_at")

    return render(
        request,
        "foodapp/orders.html",
        {
            "orders": orders
        }
    )


def payment_view(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id
    )

    qr_folder = Path(
        settings.MEDIA_ROOT
    ) / "qr"

    qr_folder.mkdir(
        parents=True,
        exist_ok=True
    )

    qr_file = qr_folder / f"order_{order.id}.png"

    upi_id = "yourupi@upi"

    upi_url = (
        f"upi://pay?"
        f"pa={upi_id}"
        f"&pn=FoodDelivery"
        f"&am={order.total_price}"
        f"&cu=INR"
        f"&tn=Order%20{order.id}"
    )

    qr = qrcode.make(upi_url)

    qr.save(qr_file)

    qr_path = (
        settings.MEDIA_URL
        + f"qr/order_{order.id}.png"
    )

    return render(
        request,
        "foodapp/payment.html",
        {
            "order": order,
            "total_amount": order.total_price,
            "qr_path": qr_path
        }
    )
def payment(request, order_id):
    order = Order.objects.get(id=order_id)

    return render(request, "payment.html", {
        "order": order
    })
def payment_success(request, order_id):
    order = Order.objects.get(id=order_id)

    return render(request, "foodapp/payment_success.html", {
        "order": order
    })



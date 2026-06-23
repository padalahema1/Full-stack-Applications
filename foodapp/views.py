from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Restaurant, MenuItem, Order


def home(request):
    restaurants = Restaurant.objects.all()

    return render(
        request,
        'foodapp/restaurants.html',
        {
            'restaurants': restaurants
        }
    )
# Show Restaurants
def restaurant_list(request):
    restaurants = Restaurant.objects.all()

    return render(
        request,
        'foodapp/restaurants.html',
        {
            'restaurants': restaurants
        }
    )


# Show Menu
def menu(request, id):
    items = MenuItem.objects.filter(restaurant_id=id)

    return render(
        request,
        'foodapp/menu.html',
        {
            'items': items
        }
    )


# Place Order
def place_order(request, id):
    item = MenuItem.objects.get(id=id)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))

        total = item.price * quantity

        Order.objects.create(
            item=item,
            quantity=quantity,
            total_price=total
        )

        return redirect('orders')

    return render(
        request,
        'foodapp/order.html',
        {
            'item': item
        }
    )


# View Orders
def orders(request):
    orders = Order.objects.all()

    return render(
        request,
        'foodapp/orders.html',
        {
            'orders': orders
        }
    )


# Payment Page
def payment_view(request, order_id):
    order = Order.objects.get(id=order_id)

    return render(
        request,
        'foodapp/payment.html',
        {
            'order': order,
            'total_amount': order.total_price,
            'qr_path': '/media/qr/sample_qr.png'
        }
    )


# Payment Success
def payment_success(request, order_id):
    order = Order.objects.get(id=order_id)

    order.status = "Paid"
    order.save()

    return render(
        request,
        'foodapp/payment_success.html',
        {
            'order': order
        }
    )
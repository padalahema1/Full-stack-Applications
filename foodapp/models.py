from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100)

    location = models.CharField(
        max_length=200,
        default="Rajahmundry"
    )

    image = models.ImageField(
        upload_to="restaurants/",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="menu_items"
    )

    name = models.CharField(max_length=100)

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0
    )

    image = models.ImageField(
        upload_to="menu/",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class Order(models.Model):
    item = models.ForeignKey(
        MenuItem,
        on_delete=models.CASCADE,
        related_name="orders"
    )

    customer_name = models.CharField(
        max_length=100,
        default="Guest"
    )

    quantity = models.PositiveIntegerField(
        default=1
    )

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        default="Pending"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.customer_name} - {self.item.name}"

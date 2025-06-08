from django.db import models


class Bin(models.Model):
    title = models.CharField(max_length=128, primary_key=True)
    inventory = models.PositiveIntegerField(default=0)
    brand = models.CharField(max_length=128)
    size = models.PositiveIntegerField()
    color = models.CharField(max_length=32)
    price = models.PositiveIntegerField()
    dimensions = models.CharField(max_length=16, blank=True, default='')
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.title


class Order(models.Model):
    STATUS_CHOICES = [
        ('p', 'در انتظار'),
        ('s', 'ارسال شده'),
    ]

    customer_name = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=11)
    address = models.TextField()
    postal_code = models.CharField(max_length=32)
    total_price = models.PositiveIntegerField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='p')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"#{self.id} - {self.customer_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    bin = models.ForeignKey(Bin, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.bin.title}"

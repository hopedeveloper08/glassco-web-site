from django.db import models


class Bin(models.Model):
    title = models.CharField(max_length=128, primary_key=True, verbose_name='عنوان')
    inventory = models.PositiveIntegerField(default=0, verbose_name='موجودی')
    brand = models.CharField(max_length=128, verbose_name='برند')
    size = models.PositiveIntegerField(verbose_name='سایز')
    color = models.CharField(max_length=32, verbose_name='رنگ')
    price = models.PositiveIntegerField(verbose_name='قیمت')
    dimensions = models.CharField(max_length=16, blank=True, default='', verbose_name='ابعاد')
    image = models.ImageField(upload_to='products/', verbose_name='عکس')

    class Meta:
        verbose_name = 'سطل'
        verbose_name_plural = 'سطل'

    def __str__(self):
        return self.title


class Order(models.Model):
    STATUS_CHOICES = [
        ('p', 'در انتظار'),
        ('s', 'ارسال شده'),
    ]

    customer_name = models.CharField(max_length=32, verbose_name='نام مشتری')
    phone_number = models.CharField(max_length=11, verbose_name='شماره تلفن')
    address = models.TextField(verbose_name='آدرس')
    postal_code = models.CharField(max_length=32, verbose_name='کد پستی')
    total_price = models.PositiveIntegerField(verbose_name='قیمت کل')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='p', verbose_name='وضعیت')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')

    class Meta:
        verbose_name = 'سفارشات'
        verbose_name_plural = 'سفارشات'
    
    def __str__(self):
        return f"#{self.id} - {self.customer_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name='سفارش')
    bin = models.ForeignKey(Bin, on_delete=models.PROTECT, verbose_name='سطل')
    quantity = models.PositiveIntegerField(verbose_name='تعداد')

    def __str__(self):
        return f"{self.quantity} x {self.bin.title}"

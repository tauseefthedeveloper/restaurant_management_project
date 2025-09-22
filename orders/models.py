from django.db import models

# Create your models here.
class OrderStatus(models.Model):
    name = models.CharField(max_length=50, unique= True)
    class Meta:
        verbose_name = "Order Status"
        verbose_name_plural = "Order Statuses"

    def __str__(self):
        return self.name

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DeciamlField(max_digits=10, decimal_places=2)
    status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"

class MenuCategory(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name
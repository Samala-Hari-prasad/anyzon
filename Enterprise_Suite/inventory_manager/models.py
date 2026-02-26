from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=50, unique=True)
    category = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    min_stock_level = models.IntegerField(default=10)
    last_updated = models.DateTimeField(auto_now=True)

    @property
    def status(self):
        if self.quantity <= 0:
            return "Out of Stock"
        elif self.quantity < self.min_stock_level:
            return "Low Stock"
        else:
            return "In Stock"

    def __str__(self):
        return self.name

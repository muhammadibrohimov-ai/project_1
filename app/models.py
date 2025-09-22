from django.db import models

# Create your models here.

# User model
class User(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    year = models.PositiveIntegerField()
    address = models.CharField(null=True)
    salary = models.DecimalField(max_length=10, max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
# Category model
class Category(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
# Product model
class Product(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(null=True)
    price = models.DecimalField(max_length=10, max_digits=8, decimal_places=3)
    quantity = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)
    
    def __str__(self):
        return self.name
    
# Order model
class Orders(models.Model):
    STATUS_CHOICES = [
        ['in proccess', "In proccess"],
        ['canceled', 'Canceled'],
        ['finished', 'Finished'],
        ['pending', 'Pending']
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Order #{self.id} - {self.user.name}"
    
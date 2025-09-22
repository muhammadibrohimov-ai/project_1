from django.contrib import admin

# Register your models here.

from .models import User, Category, Product, Order

admin.site.register([User, Category, Product, Order])

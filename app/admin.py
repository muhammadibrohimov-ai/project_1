from django.contrib import admin

# Register your models here.

from .models import User, Category, Product, Orders

admin.site.register([User, Category, Product, Orders])

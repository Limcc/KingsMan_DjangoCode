from django.contrib import admin
from .models import product

# Register your models here.
class product_admin(admin.ModelAdmin):
    fields = ["photo", "name", "price", "category"]

admin.site.register(product, product_admin)
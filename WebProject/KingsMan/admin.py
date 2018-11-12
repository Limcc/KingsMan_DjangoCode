from django.contrib import admin
from .models import product, productPhoto

# Register your models here.
class product_admin(admin.ModelAdmin):
    fields = ["photo", "name", "price", "category"]

class productPhoto_admin(admin.ModelAdmin):
    fields = ["code", "photo"]

admin.site.register(product, product_admin)
admin.site.register(productPhoto, productPhoto_admin)
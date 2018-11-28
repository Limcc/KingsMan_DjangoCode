from django.contrib import admin
from .models import product, productPhoto, cart

# Register your models here.
class product_admin(admin.ModelAdmin):
    fields = ["photo", "name", "price", "category"]

class productPhoto_admin(admin.ModelAdmin):
    fields = ["code", "photo"]

class cart_admin(admin.ModelAdmin):
    fields = ["userName", "name", "size"]

admin.site.register(product, product_admin)
admin.site.register(productPhoto, productPhoto_admin)
admin.site.register(cart, cart_admin)

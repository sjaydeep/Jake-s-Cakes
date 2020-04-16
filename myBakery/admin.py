from django.contrib import admin
from myBakery.models import Contact,Product, Order, OrderUpdate, Profile, BirthdayProduct, WeddingProduct
# Register your models here.
admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderUpdate)
admin.site.register(Profile)
admin.site.register(BirthdayProduct)
admin.site.register(WeddingProduct)
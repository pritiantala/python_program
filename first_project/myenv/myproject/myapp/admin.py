from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Shopkeeper)
admin.site.register(Customer)
admin.site.register(Products)
admin.site.register(RAMSpecification)
admin.site.register(Offers)
admin.site.register(MyCart)
admin.site.register(ProceedProduct)
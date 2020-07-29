from django.contrib import admin
from .models import products, Profile, userorders
# Register your models here.

admin.site.register(products)
admin.site.register(userorders)
admin.site.register(Profile)

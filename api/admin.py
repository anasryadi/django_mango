from django.contrib import admin
from .models.mango import Mango
from .models.mango_shop import MangoShop

# Register your models here.
admin.site.register(Mango)
admin.site.register(MangoShop)
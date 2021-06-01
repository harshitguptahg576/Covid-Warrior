from django.contrib import admin

from .models import Medicine
from .models import Product

admin.site.register(Medicine)
admin.site.register(Product)

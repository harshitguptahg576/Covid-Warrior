from django.contrib import admin

from .models import Medicine
from .models import Product
from .models import Center

admin.site.register(Medicine)
admin.site.register(Product)
admin.site.register(Center)

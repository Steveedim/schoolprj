from django.contrib import admin
from .models import People, Category
# Register your models here.

admin.site.register(Category)
admin.site.register(People)
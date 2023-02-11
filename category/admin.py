# greatkart (outer project folder)/ category folder/ admin.py

from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    # since its a tuple, put comma in the end
    prepopulated_fields = {"slug": ("category_name",)} 
    list_display = ("category_name", "slug")

admin.site.register(Category, CategoryAdmin)

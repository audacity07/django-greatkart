# greatkart (outer project folder)/ category folder/ apps.py

from django.apps import AppConfig


class CategoryConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "category"

# greatkart (outer project folder)/ carts folder/ apps.py

from django.apps import AppConfig


class CartsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "carts"

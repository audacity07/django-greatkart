# greatkart (outer project folder)/ greatkart (inner project folder)/ views.py

from django.shortcuts import render
from store.models import Product, ReviewRating

def home(request):
    # we need only those products which are available
    products = Product.objects.all().filter(is_available=True).order_by("created_date")

    # Get the reviews
    reviews = None
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    context = {
        "products": products,
        "reviews": reviews,
    }
    return render(request, "home.html", context)
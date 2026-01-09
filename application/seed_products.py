import os
import sys
import django

# ADD PROJECT ROOT TO PYTHON PATH
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# SET DJANGO SETTINGS MODULE
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blinkit.settings")

django.setup()

from application.models import product

products = [
    product(
        name="apple",
        image="image/apple.jpg",
        description="Crunchy and mildly sweet fruit available in various varieties, great for snacking and salads.",
        rating=3.2,
        price=30,
        categories="fruits",
        weight_kg="1"
    ),
    product(
        name="banana",
        image="image/banana.jpg",
        description="Soft, sweet fruit with a yellow peel, commonly eaten fresh or used in shakes and snacks.",
        rating=3.7,
        price=65,
        categories="fruits",
        weight_kg="1"
    ),
    # add more if you want
]

product.objects.bulk_create(products)

print(f"{len(products)} products inserted successfully")


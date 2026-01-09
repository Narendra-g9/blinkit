import os
import django

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
    product(
        name="cherry",
        image="image/cherry.jpg",
        description="Small, sweet, and juicy red fruit often used in desserts and beverages.",
        rating=3.4,
        price=40,
        categories="fruits",
        weight_kg="1"
    ),
    product(
        name="kiwi",
        image="image/kiwi.jpg",
        description="Small fuzzy fruit with tangy green flesh rich in vitamin C and antioxidants.",
        rating=3.4,
        price=50,
        categories="fruits",
        weight_kg="1"
    ),
    product(
        name="watermelon",
        image="image/watermelon.jpg",
        description="Large juicy fruit with high water content, ideal for hydration and summer refreshment.",
        rating=3.9,
        price=35,
        categories="fruits",
        weight_kg="1"
    ),
    # 👉 YOU CAN CONTINUE ADDING THE REST THE SAME WAY
]

product.objects.bulk_create(products)

print(f"{len(products)} products inserted successfully")

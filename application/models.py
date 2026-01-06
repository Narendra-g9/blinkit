from django.db import models

class product(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='image')
    description=models.TextField()
    rating=models.FloatField()
    price=models.FloatField()
    categories=models.CharField(max_length=255)
    create_at=models.DateField(auto_now=True)
    update_at=models.DateField(auto_now_add=True)
    weight_kg=models.TextField()

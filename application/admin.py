from django.contrib import admin
from application.models import product
class product_1(admin.ModelAdmin):
    list_display=['id','name','image','description','rating','price','categories','create_at','update_at','weight_kg']
    
admin.site.register(product,product_1)
  

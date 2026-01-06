"""
URL configuration for blinkit project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from application import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('show/<int:id>/<str:categories>/',views.show,name='show'),
    path('cart_list/<int:id>/',views.cart_list,name="cart_list"),
    path('show_cart/',views.show_cart,name='show_cart'),
    path('remove_cart/<int:id>/',views.remove_cart,name='remove_cart'),
    path('',views.login1,name='login1'),
    path('register1',views.register1,name='register1'),
    path('filter_data',views.filter_data,name='filter_data'),
    path('categories/<str:categories>/',views.categories,name='categories'),
    path('order1',views.order1,name='order1'),
    path('pay1/<int:id>/',views.pay1,name='pay1')
  
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



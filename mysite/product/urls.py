from django.urls import path
from . import views

urlpatterns = [
    #Home
    #path('', views.home, name='home'),

    #Product
    path('product/register', views.register_product, name='register_product'),
    path('product/list/<int:id>', views.list_product, name='list_product'),
    path('product/update/<int:id>', views.update_product, name='update_product'),
    path('product/delete/<int:id>', views.delete_product, name='delete_product'),
]
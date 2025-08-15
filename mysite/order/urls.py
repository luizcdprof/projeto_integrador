from django.urls import path
from . import views

urlpatterns = [
    #Home
    #path('', views.home, name='home'),

    #Order
    path('order/create', views.create_order, name='create_order'),
    path('order/list/<int:id>', views.list_order_by_id, name='list_order_by_id'),
    path('order/list', views.list_order, name='list_order'),
    path('order/update/<int:id>', views.update_order, name='update_order'),
    path('order/delete/<int:id>', views.delete_order, name='delete_order'),
    path('order/add_item/<int:id>', views.add_item_order, name='add_item_order'),
    path('order/remove_item/<int:id>', views.remove_item_order, name='remove_item_order'),
]
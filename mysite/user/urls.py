from django.urls import path
from . import views

urlpatterns = [
    #Profile
    path('profile/register', views.register_profile, name='register_profile'),
    path('profile/list/<int:id>', views.list_profile, name='list_profile'),
    path('profile/update/<int:id>', views.update_profile, name='update_profile'),
    path('profile/delete/<int:id>', views.delete_profile, name='delete_profile'),
]
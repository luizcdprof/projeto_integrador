from django.urls import path
from . import views
from .views import HomeView
#from django.views.generic.base import TemplateView

urlpatterns = [
    #Home
    #path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', HomeView.as_view(), name='home')
]
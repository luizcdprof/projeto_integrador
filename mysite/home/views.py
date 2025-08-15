from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nome"] = "Rian"  # ou qualquer outra lógica/dado
        return context

def home(request):
    return render(request, 'home.html', {'nome': 'Rian'})
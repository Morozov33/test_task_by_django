from django.views.generic.base import TemplateView
from menu_builder.models import menu


class HomeView(TemplateView):
    template_name = 'home.html'
    extra_context = {'menus': menu.objects.all()}
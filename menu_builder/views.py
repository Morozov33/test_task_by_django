from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'


class PageView(TemplateView):
    template_name = 'page.html'


class Page_2View(TemplateView):
    template_name = 'page_2.html'

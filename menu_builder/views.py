from django.views.generic.base import TemplateView


# View for pages in main_menu
class PageView(TemplateView):
    template_name = 'page.html'


# View for pages in docs_menu
class Page_2View(TemplateView):
    template_name = 'page_2.html'

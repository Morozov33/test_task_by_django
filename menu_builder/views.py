from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'


class TasksView(TemplateView):
    template_name = 'tasks.html'


class LabelsView(TemplateView):
    template_name = 'labels.html'

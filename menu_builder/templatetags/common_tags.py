from django import template
from menu_builder.models import menu as menu_model
from django.urls import resolve


register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name):

    path = context['request'].path
    url_list = [path, resolve(path).url_name]
    menu = menu_model.objects.filter(name=menu_name).get_descendants(include_self=True)
    current_tree_path = menu_model.objects.filter(url__in=url_list).get_ancestors(include_self=True)
    nodes_path = [node.name for node in current_tree_path]

    return {
        "menu": menu,
        "menu_name": menu_name,
        "path": path,
        "nodes_path": nodes_path,
    }

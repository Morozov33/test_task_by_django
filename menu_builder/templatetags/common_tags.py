from django import template
from menu_builder.models import menu as menu_model
from django.urls import resolve


register = template.Library()


# register new common tag
@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name):

    # get current path
    path = context['request'].path

    # in url_list both path: named url and absolute url
    url_list = [path, resolve(path).url_name]

    # get tree from DB
    menu = menu_model.objects.all()

    # get current node from tree model
    current_node = menu_model.objects.filter(url__in=url_list)

    # get tree-path of ansestors of current node
    current_node_tree = current_node.get_ancestors(include_self=True)

    # make list of names all nodes from tree-path of current node
    nodes_path = [node.name for node in current_node_tree]

    # returns values in template tag
    return {
        "menu": menu,
        "menu_name": menu_name,
        "path": path,
        "nodes_path": nodes_path,
        "menu_id": 0,
    }

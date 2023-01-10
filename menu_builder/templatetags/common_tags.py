from django import template
from menu_builder.models import menu as menu_model
from django.urls import resolve


register = template.Library()


def get_nodes_path(tree, urls, menu_name, parent_id=None):
    # returns a list of node.id, that corresponds to
    # the path to the current point menu
    path = []
    for node in tree:
        if (node.name == menu_name or node.level != 0) and node.url in urls:
            path.append(node.id)
            parent_id = node.parent_id

    def get_all_parents(tree, path, parent_id):
        for node in tree:
            if node.id == parent_id:
                path.append(node.id)
                get_all_parents(tree, path, node.parent_id)

    get_all_parents(tree, path, parent_id)
    return path


# register new common tag
@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name):

    # get current path
    path = context['request'].path

    # in url_list both path: named url and absolute url
    urls = (path, resolve(path).url_name)

    # get tree from DB
    menu = menu_model.objects.all()

    # returns values in template tag
    return {
        "menu": menu,
        "menu_name": menu_name,
        "path": path,
        "nodes_path": get_nodes_path(menu, urls, menu_name),
    }

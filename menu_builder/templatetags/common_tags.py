from django import template
from menu_builder.models import menu as menu_model
register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name):
    menu_root = menu_model.objects.filter(name=menu_name)
    menu = menu_root.get_descendants(include_self=False)
    return {
        "menu": menu,
        "menu_name": menu_name,
        "request": context['request'],
    }

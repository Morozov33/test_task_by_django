from django import template
from menu_builder.models import menu
register = template.Library()


@register.inclusion_tag('menu.html')
def draw_menu(menu_name):
    menu_root = menu.objects.filter(name=menu_name)
    menu_ = menu_root.get_descendants(include_self=True)
    return {
        "menu_": menu_,
        "menu_name": menu_name,
    }

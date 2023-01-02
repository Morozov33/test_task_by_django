from django import template
from menu_builder.models import menu
register = template.Library()


@register.inclusion_tag('menu.html')
def draw_menu(name_menu):
    menu_root = menu.objects.filter(name=name_menu)
    menu_ = menu_root.get_descendants(include_self=True)
    return {
        "menu_": menu_,
    }

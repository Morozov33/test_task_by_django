from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from menu_builder.models import menu


admin.site.register(
    menu,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    ),
)

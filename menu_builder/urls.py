"""menu_builder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from menu_builder.views import HomeView, PageView, Page_2View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('catalog/', PageView.as_view(), name='catalog'),
    path('support/', PageView.as_view(), name='support'),
    path('docs/', TemplateView.as_view(template_name='docs.html'),
         name='docs'),
    path('catalog/category_1/', PageView.as_view(), name='category_1'),
    path('catalog/category_2/', PageView.as_view(), name='category_2'),
    path('catalog/category_1/subcategory_1/',
         PageView.as_view(), name='subcategory_1'),
    path('catalog/category_1/subcategory_2/',
         PageView.as_view(), name='subcategory_2'),
    path('catalog/category_2/subcategory_3/',
         PageView.as_view(), name='subcategory_3'),
    path('catalog/category_2/subcategory_4/',
         PageView.as_view(), name='subcategory_4'),
    path('catalog/category_1/subcategory_1/product_1/',
         PageView.as_view(), name='product_1'),
    path('catalog/category_1/subcategory_1/product_2/',
         PageView.as_view(), name='product_2'),
    path('catalog/category_1/subcategory_2/product_3/',
         PageView.as_view(), name='product_3'),
    path('catalog/category_1/subcategory_2/product_4/',
         PageView.as_view(), name='product_4'),
    path('catalog/category_2/subcategory_3/product_5/',
         PageView.as_view(), name='product_5'),
    path('catalog/category_2/subcategory_4/product_6/',
         PageView.as_view(), name='product_6'),
    path('catalog/support/support_report/',
         PageView.as_view(), name='support_report'),
    path('catalog/support/support_tasks/',
         PageView.as_view(), name='support_tasks'),
    path('catalog/support/support_report/report_1/',
         PageView.as_view(), name='report_1'),
    path('catalog/support/support_report/report_2/',
         PageView.as_view(), name='report_2'),
    path('catalog/support/support_tasks/task_1/',
         PageView.as_view(), name='task_1'),
    path('catalog/support/support_tasks/task_2/',
         PageView.as_view(), name='task_2'),
    path('docs/install/', Page_2View.as_view(), name='install'),
    path('docs/install/install_guide/',
         Page_2View.as_view(), name='install_guide'),
    path('docs/tutorial/', Page_2View.as_view(), name='tutorial'),
    path('docs/tutorial/tutorial_part_1/',
         Page_2View.as_view(), name='tutorial_part_1'),
    path('docs/tutorial/tutorial_part_2/',
         Page_2View.as_view(), name='tutorial_part_2'),
    path('docs/tutorial/docs/change_logs/',
         Page_2View.as_view(), name='change_logs'),
    path('docs/tutorial/docs/change_logs/change_logs/2022/',
         Page_2View.as_view(), name='change_logs_2022'),
    path('docs/tutorial/docs/change_logs/change_logs/2023/',
         Page_2View.as_view(), name='change_logs_2023'),
    path('docs/issues/', Page_2View.as_view(), name='issues'),
    path('docs/issues/issues/1/', Page_2View.as_view(), name='issue_1'),
    path('docs/issues/issues/2/', Page_2View.as_view(), name='issue_2'),
]

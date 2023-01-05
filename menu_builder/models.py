from django.db import models
from django.urls import reverse, NoReverseMatch
from mptt.models import MPTTModel, TreeForeignKey


class menu(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    url = models.CharField(max_length=255, verbose_name="URL", null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return f"{self.name}"

    class MPTTMeta:
        order_insertion_by = ['name',]

    def get_url(self):
        if self.url:
            try:
                return reverse(self.url)
            except NoReverseMatch:
                return self.url

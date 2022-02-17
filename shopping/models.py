
from django_extensions.db.fields import AutoSlugField

from django.db import models
from django.utils.translation import gettext as _


class Category(models.Model):
    CATEGORY_TYPES = (
        ("D", _("Department")),
        ("I", _("Item")),
    )

    name = models.CharField(max_length=255)
    slug = AutoSlugField(max_length=128, populate_from=["name"])
    category_type = models.CharField(
        max_length=1,
        choices=CATEGORY_TYPES,
        default="I",
        verbose_name=_("Type")
    )

    class Meta:
        unique_together = ('name', 'category_type',)

    def __str__(self):
        return self.name


class ShoppingItem(models.Model):
    description = models.CharField(max_length=255)
    slug = AutoSlugField(max_length=128, populate_from=["description"])
    quantity = models.PositiveIntegerField()
    category = models.ForeignKey(
        Category,
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.description

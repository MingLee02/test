from django.urls import path
from . import views


urlpatterns = [
    path(
        "shopping-item",
        views.ShoppingItemsListView.as_view(),
        name="shopping_items"
    ),
    path(
        "shopping-item/delete/<slug>",
        views.ShoppingItemDeleteView.as_view(),
        name="shopping_item_delete"
    ),
    path(
        "shopping-item/create",
        views.ShoppingItemCreateView.as_view(),
        name="shopping_item_create"
    ),
    path(
        "shopping-item/update/<slug>",
        views.ShoppingItemUpdateView.as_view(),
        name="shopping_item_update"
    ),
    path(
        "category/create",
        views.CategoryCreateView.as_view(),
        name="category_create"
    ),
    path(
        "category/<slug>",
        views.CategoryDetailView.as_view(),
        name="category_detail"
    ),
    path(
        "category/delete/<slug>",
        views.CategoryDeleteView.as_view(),
        name="category_delete"
    ),
    path(
        "category/update/<slug>",
        views.CategoryUpdateView.as_view(),
        name="category_update"
    ),
]

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
    DetailView
)


from .models import ShoppingItem, Category
from .forms import ShoppingItemForm, CategoryForm


class ShoppingItemsListView(ListView):
    template_name = "shopping-items-list-page.html"
    model = ShoppingItem
    context_object_name = 'shoppingItem'


class ShoppingItemDeleteView(DeleteView):
    model = ShoppingItem
    template_name = 'confirm-delete.html'

    def get_success_url(self):
        messages.success(self.request, "deleted successfully")
        return reverse_lazy('shopping_items')


class ShoppingItemCreateView(CreateView):
    template_name = "shopping-item-add.html"
    form_class = ShoppingItemForm
    model = ShoppingItem

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Add shopping item'

        return context

    def get_success_url(self):
        messages.success(self.request, "created successfully")
        return reverse_lazy('shopping_items')


class ShoppingItemUpdateView(UpdateView):
    model = ShoppingItem
    form_class = ShoppingItemForm
    template_name = 'shopping-item-add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Update shopping item'

        return context

    def get_success_url(self):
        messages.success(self.request, "updated successfully")
        return reverse_lazy('shopping_items')


class CategoryCreateView(CreateView):
    template_name = "category-add.html"
    form_class = CategoryForm
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Add Category'

        return context

    def get_success_url(self):
        messages.success(self.request, "created successfully")
        return reverse_lazy('shopping_items')


class CategoryDetailView(DetailView):
    template_name = "category-detail.html"
    model = Category
    context_object_name = 'category'


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'confirm-delete.html'

    def get_success_url(self):
        messages.success(self.request, "deleted successfully")
        return reverse_lazy('shopping_items')


class CategoryUpdateView(UpdateView):
    template_name = "category-add.html"
    form_class = CategoryForm
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Update Category'

        return context

    def get_success_url(self):
        messages.success(self.request, "updated successfully")
        return reverse_lazy('shopping_items')

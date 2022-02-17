from django.views.generic import View
from django.shortcuts import redirect
from django.urls import reverse


class Home(View):
    def get(self, request):
        return redirect(reverse('shopping_items'))

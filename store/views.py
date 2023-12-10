from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import DATABASE

# Create your views here.

class productsView(View):
    def get(self,requests):
        return JsonResponse(DATABASE, json_dumps_params={'ensure_ascii': False,
                                                     'indent': 4})       

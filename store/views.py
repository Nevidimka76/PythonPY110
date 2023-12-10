from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
from .models import DATABASE

# def shop_view(request):
#     if request.method == "GET":
#         with open('store/shop.html', encoding="utf-8") as f:
#             data = f.read()  # Читаем HTML файл
#         return HttpResponse(data)
# Create your views here.

class shopView(View):
    def get(self,requests):
        with open('store/shop.html', encoding="utf-8") as f:
            data = f.read()  # Читаем HTML файл
        return HttpResponse(data)
        

class productsView(View):
    def get(self,requests):
        return JsonResponse(DATABASE, json_dumps_params={'ensure_ascii': False,
                                                     'indent': 4})       

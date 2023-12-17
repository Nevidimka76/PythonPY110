from django.shortcuts import render

from django.http import JsonResponse, HttpResponse, HttpResponseNotFound 
from django.views import View
from .models import DATABASE as db

# Create your views here.

class shopView(View):
    def get(self,requests):
        with open('store/shop.html', encoding="utf-8") as f:
            data = f.read()  # Читаем HTML файл
        return HttpResponse(data)
        

class productsView(View):
    def get(self,rqst):
        id_=rqst.GET.get('id')
        if id_:
            product=db.get(id_)
            if product:
                data=db[id_]
            else:
                return HttpResponseNotFound('Данного продукта нет в БД!')
        else:
            data=db
            
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False,
                                                     'indent': 4})  
class productsPageView(View):
    def get(self,reqst,page):
        if isinstance(page,str):
            for data in db.values():
                if data['html']==page:
                    with open(f'store/products/{page}.html', encoding="utf-8") as f:
                        data = f.read()  # Читаем HTML файл
                    return HttpResponse(data)
        elif isinstance(page,int):
                if data:=db.get(str(page)):
                    with open(f"store/products/{data['html']}.html", encoding="utf-8") as f:
                        data = f.read()  # Читаем HTML файл
                    return HttpResponse(data)
            
        return HttpResponseNotFound('Описания товара нет')
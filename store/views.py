from django.shortcuts import render

from django.http import JsonResponse, HttpResponse, HttpResponseNotFound 
from django.views import View
from .models import DATABASE as db
from logic.services import filtering_category,viewInCart,addToCart,removeFromCart

# Create your views here.

class shopView(View):
    def get(self,requests):
        with open('store/shop.html', encoding="utf-8") as f:
            data = f.read()  # Читаем HTML файл
        return HttpResponse(data)
        

class productsView(View):
    def get(self,rqst):
        #id_=rqst.GET.get('id')
        if id_ := rqst.GET.get('id'):
            product=db.get(id_)
            if product:
                data=db[id_]
            else:
                return HttpResponseNotFound('Данного продукта нет в БД!')
        else:
            data=db
            
        if category_key := rqst.GET.get("category"):  # Считали 'category' 
            if ordering_key := rqst.GET.get("ordering"): # Если в параметрах есть 'ordering'
                if rqst.GET.get("reverse") in ('true', 'True'): # Если в параметрах есть 'ordering' и 'reverse'=True
                    data = filtering_category(db,category_key,ordering_key,True) #  TODO Провести фильтрацию с параметрами
                else:
                    data = filtering_category(db,category_key,ordering_key) #  TODO Провести фильтрацию с параметрами
            else:
                data = filtering_category(db,category_key) #  TODO Провести фильтрацию с параметрами
            # В этот раз добавляем параметр safe=False, для корректного отображения списка в JSON
            return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False,
                                                                 'indent': 4})

        # return JsonResponse(data, json_dumps_params={'ensure_ascii': False,
        #                                              'indent': 4})  


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
    
class cartView(View):
    def get(self,rqst):
        data=viewInCart()
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False,
                                                     'indent': 4})


class cartAddView(View):
    def get(self,rqst,idProduct):
        result=addToCart(idProduct,db)
        if result:
            return JsonResponse({"answer": "Продукт успешно добавлен в корзину"},
                                json_dumps_params={'ensure_ascii': False})

        return JsonResponse({"answer": "Неудачное добавление в корзину"},
                            status=404,
                            json_dumps_params={'ensure_ascii': False})


class cartDelView(View):
    def get(self,rqst,idProduct):
        result=removeFromCart(idProduct)
        if result:
            return JsonResponse({"answer": "Продукт успешно удалён из корзины"},
                                json_dumps_params={'ensure_ascii': False})

        return JsonResponse({"answer": "Неудачное удаление из корзины"},
                            status=404,
                            json_dumps_params={'ensure_ascii': False})    
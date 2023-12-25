from django.shortcuts import render

from django.http import JsonResponse, HttpResponse, HttpResponseNotFound 
from django.views import View
from .models import DATABASE as db
from logic.services import filtering_category,viewInCart,addToCart,removeFromCart

# Create your views here.

# class shopView(View):
#     def get(self,requests):
#         with open('store/shop.html', encoding="utf-8") as f:
#             data = f.read()  # Читаем HTML файл
#         return HttpResponse(data)
        
class shopView(View):
    def get(self,rqst):
        if category_key := rqst.GET.get("category"):  # Считали 'category' 
            if ordering_key := rqst.GET.get("ordering"): # Если в параметрах есть 'ordering'
                if rqst.GET.get("reverse") in ('true', 'True'): # Если в параметрах есть 'ordering' и 'reverse'=True
                    data = filtering_category(db,category_key,ordering_key,True) #  TODO Провести фильтрацию с параметрами
                else:
                    data = filtering_category(db,category_key,ordering_key) #  TODO Провести фильтрацию с параметрами
            else:
                data = filtering_category(db,category_key) #  TODO Провести фильтрацию с параметрами
        else:
            data=db.values()
        # return render(rqst,'store/shop.html',context={'products': db.values()})
        return render(rqst,'store/shop.html',context={'products': data,
                                                       'category': category_key})
    

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
    def get(self,rqst,page):
        if isinstance(page,str):
            for product in db.values():
                if product['html']==page:
                    category=product['category']
                    other=[data for data in db.values if data[category]==category and data!=product]
                    return render(rqst, "store/product.html", context={"product": product, 
                                                                       "other": other})
                    # with open(f'store/products/{page}.html', encoding="utf-8") as f:
                    #     data = f.read()  # Читаем HTML файл
                    # return HttpResponse(data)
        elif isinstance(page,int):
                if product:=db.get(str(page)):
                    category=product['category']
                    other=[data for data in db.values() if data['category'] == category and data != product]
                    return render(rqst, "store/product.html", context={"product": product, 
                                                                       "other": other})
                    
                    # return render(rqst, "store/product.html", context={"product": data})
                    # with open(f"store/products/{data['html']}.html", encoding="utf-8") as f:
                    #     data = f.read()  # Читаем HTML файл
                    # return HttpResponse(data)
            
        return HttpResponseNotFound('Описания товара нет')
    
class cartView(View):
    def get(self,rqst):
        data=viewInCart()
        if rqst.GET.get('format') == 'JSON':
            return JsonResponse(data, json_dumps_params={'ensure_ascii': False,
                                                         'indent': 4})
        products=[]
        for product_id, quantity in data['products'].items():
            product=db.get(product_id)
            product['quantity']=quantity
            product['price_total']=f"{quantity*product['price_after']:2f}"
            products.append(product)
        return render(rqst,'store/cart.html', context={'products': products})
    

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
from django.shortcuts import render, redirect
#from django.views.generic import ListView
from django.views import View
from django.contrib.auth import get_user
from logic.services import viewInWish,addToWish,removeFromWish
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound 
from store.models import DATABASE as db
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

   

class wishlistView(View):
    @method_decorator(login_required(login_url='login:login_view'))
    def get(self,rqst):
        user=get_user(rqst).username
        data=viewInWish(rqst)[user]
        if rqst.GET.get('format') == 'JSON':
            return JsonResponse(data, json_dumps_params={'ensure_ascii': False,
                                                         'indent': 4})
        products=[]
        for product_id in data['products']:
            product=db.get(product_id)
            product['price_total']=f"{product['price_after']:2f}"
            products.append(product)
        return render(rqst,'wishlist/wishlist.html', context={'products': products})
        
        # current_user=get_user(rqst).username
        #     return render(rqst, "wishlist/wishlist.html")
        
class wishlistAddView(View):
#    @method_decorator(login_required(login_url='login:login_view'))
    def get(self,rqst,idProduct):
        result=addToWish(rqst,idProduct,db)
        if result:
            return JsonResponse({"answer": "Продукт успешно добавлен в избранное"},
                                json_dumps_params={'ensure_ascii': False})

        return JsonResponse({"answer": "Неудачное добавление в корзину"},
                            status=404,
                            json_dumps_params={'ensure_ascii': False})


class wishlistDelView(View):
#    @method_decorator(login_required(login_url='login:login_view'))
    def get(self,rqst,idProduct):
        result=removeFromWish(rqst,idProduct)
        if result:
            return JsonResponse({"answer": "Продукт успешно удалён из корзины"},
                                json_dumps_params={'ensure_ascii': False})

        return JsonResponse({"answer": "Неудачное удаление из корзины"},
                            status=404,
                            json_dumps_params={'ensure_ascii': False})    

class wishlistJSON(View):
    def get(self,rqst):
        user=get_user(rqst).username
        data=viewInWish(rqst)[user]
        if data:
            return JsonResponse(data, json_dumps_params={'ensure_ascii': False,
                                                         'indent': 4})


class wishRemoveView(View):
    def get(self,rqst,idProduct):
        result=removeFromWish(rqst,idProduct)
        if result:
            return redirect("wishlist:wishList")
        return HttpResponseNotFound("Неудачное удаление из корзины")    

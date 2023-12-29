from django.shortcuts import render, redirect
#from django.views.generic import ListView
from django.views import View
from django.contrib.auth import get_user
from logic.services import viewInWish
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound 
from store.models import DATABASE as db
# Create your views here.

   

class wishlistView(View):
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
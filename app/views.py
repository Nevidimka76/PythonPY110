from django.shortcuts import render
from random import random
from django.http import HttpResponse, JsonResponse, FileResponse
from datetime import datetime
from django.views import View
from .models import db

def random_view(request):
    if request.method == "GET":
        data = random()
        return HttpResponse(data)


def datetime_view(request):
    if request.method == "GET":
        data =datetime.now().strftime('%d.%m.%y %H:%M:%S')
        return HttpResponse(data)
    
def fileView(request):
    if request.method == "GET":
        return FileResponse(open('x_sq_y.png','rb'))


class dateView(View): 
   def get(self, requests,d=None,m=None,year=None):
        data =datetime.now().strftime('%d-%m-%y %H:%M:%S')
        if year is not None:
            filterDB=[post['post'] for post in db if post['year']>int(year)]
        else:
            filterDB=[post['post'] for post in db]
        data={"Имя": "Дмитрий",'time':data, 'posts':filterDB}
        return JsonResponse(data,json_dumps_params={'ensure_ascii': False})
        

# Create your views here.

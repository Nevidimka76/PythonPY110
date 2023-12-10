from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse
from datetime import datetime
from django.views import View


db=[{'year':2021,'post':'one21'},
    {'year':2022,'post':'one22'},
    {'year':2021,'post':'two21'},
    {'year':2022,'post':'two22'},
    {'year':2020,'post':'one20'},
    {'year':2020,'post':'two20'},
]


def datetime_view(request):
    if request.method == "GET":
        data =datetime.now().strftime('%d.%m.%y %H:%M:%S')
        return HttpResponse(data)
    
def fileView(request):
    if request.method == "GET":
        return FileResponse(open('x_sq_y.png','rb'))


class dateView(View):
   def get(self, requests,year=None):
        data =datetime.now().strftime('%d-%m-%y %H:%M:%S')
        if year is not None:
            filterDB=[post['post'] for post in db if post['year']>year]
        else:
            filterDB=[post['post'] for post in db]
        data={"Имя": "Дмитрий",'time':data, 'posts':filterDB}
        return JsonResponse(data,json_dumps_params={'ensure_ascii': False})
        
# Create your views here.

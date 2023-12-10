from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.views import View

def datetime_view(request):
    if request.method == "GET":
        data =datetime.now().strftime('%d.%m.%y %H:%M:%S')
        return HttpResponse(data)
    
class dateView(View):
   def get(self, requests):
        data =datetime.now().strftime('%d-%m-%y %H:%M:%S')
        return HttpResponse(data)
        
# Create your views here.

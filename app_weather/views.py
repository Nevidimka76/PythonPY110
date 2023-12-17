from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
#import requests as rq
from django.views import View
import weather_api as wthr


# def weather_view(request):
#     if request.method == "GET":
#         lat = request.GET.get('lat')  # данные придут в виде строки
#         lon = request.GET.get('lon')  # данные придут в виде строки
#         if lat and lon:
#             data = current_weather(lat=lat, lon=lon)
#         else:
#             data = current_weather(59.93, 30.31)
#         return JsonResponse(data, json_dumps_params={'ensure_ascii': False,
#                                                     'indent': 4})

class viewCurrentWeather(View):
    def get(self,rqst):
        lat = rqst.GET.get('lat')  # данные придут в виде строки
        lon = rqst.GET.get('lon')  # данные придут в виде строки
        if lat and lon:
            data = wthr.current_weather(lat=lat, lon=lon)
        else:
            data = wthr.current_weather(56.6, 84.89)
        
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False,
                                                     'indent': 4})       
        


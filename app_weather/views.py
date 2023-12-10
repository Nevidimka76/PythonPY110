from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
import requests as rq
from datetime import datetime
from django.views import View

# Словарь перевода значений направления ветра
from .models import DIRECTION_TRANSFORM

def current_weather(lat, lon):
    """
    Описание функции, входных и выходных переменных
    """
    token = '23a2989f-40a3-47fa-8f5a-9db64bf8f662'  # Вставить ваш токен
    url = f"https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}"
    headers = {"X-Yandex-API-Key": f"{token}"}
    response = rq.get(url, headers=headers)
    data = response.json()

    result = {
        'city': data['geo_object']['locality']['name'],
        'time': datetime.fromtimestamp(data['fact']['uptime']).strftime("%H:%M"),
        'temp': data['fact']['temp'],  # TODO Реализовать вычисление температуры из данных полученных от API
        'feels_like_temp': data['fact']['feels_like'],  # TODO Реализовать вычисление ощущаемой температуры из данных полученных от API
        'pressure': data['fact']['pressure_mm'],  # TODO Реализовать вычисление давления из данных полученных от API
        'humidity': data['fact']['humidity'],  # TODO Реализовать вычисление влажности из данных полученных от API
        'wind_speed': data['fact']['wind_speed'],  # TODO Реализовать вычисление скорости ветра из данных полученных от API
        'wind_gust': data['fact']['wind_gust'],  # TODO Реализовать вычисление скорости порывов ветка из данных полученных от API
        'wind_dir': DIRECTION_TRANSFORM.get(data['fact']['wind_dir']),
    }
    return result


def weather_view(request):
    if request.method == "GET":
        lat = request.GET.get('lat')  # данные придут в виде строки
        lon = request.GET.get('lon')  # данные придут в виде строки
        if lat and lon:
            data = current_weather(lat=lat, lon=lon)
        else:
            data = current_weather(59.93, 30.31)
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False,
                                                     'indent': 4})

class viewCurrentWeather(View):
    def get(self,requests):
        lat = rq.GET.get('lat')  # данные придут в виде строки
        lon = rq.GET.get('lon')  # данные придут в виде строки
        if lat and lon:
            data = current_weather(lat=lat, lon=lon)
        else:
            data = current_weather(59.93, 30.31)
        
        # token = '23a2989f-40a3-47fa-8f5a-9db64bf8f662'  # Вставить ваш токен
        # url = f"https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}"
        # headers = {"X-Yandex-API-Key": f"{token}"}
        # response = rq.get(url, headers=headers)
        # data = response.json()

        # result = {
        #     'city': data['geo_object']['locality']['name'],
        #     'time': datetime.fromtimestamp(data['fact']['uptime']).strftime("%H:%M"),
        #     'temp': data['fact']['temp'],  # TODO Реализовать вычисление температуры из данных полученных от API
        #     'feels_like_temp': data['fact']['feels_like'],  # TODO Реализовать вычисление ощущаемой температуры из данных полученных от API
        #     'pressure': data['fact']['pressure_mm'],  # TODO Реализовать вычисление давления из данных полученных от API
        #     'humidity': data['fact']['humidity'],  # TODO Реализовать вычисление влажности из данных полученных от API
        #     'wind_speed': data['fact']['wind_speed'],  # TODO Реализовать вычисление скорости ветра из данных полученных от API
        #     'wind_gust': data['fact']['wind_gust'],  # TODO Реализовать вычисление скорости порывов ветка из данных полученных от API
        #     'wind_dir': DIRECTION_TRANSFORM.get(data['fact']['wind_dir']),
        # }
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False,
                                                     'indent': 4})       
        

#    print(current_weather(59.93, 30.31))  # Проверка работы для координат Санкт-Петербурга
